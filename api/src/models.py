from main import db
import json


def is_json(json_data):
    if json_data:
        try:
            json.loads(json_data)
        except ValueError as err:
            return False
        return True
    else:
        return False


class Run(db.Model):
    __tablename__ = 'runs'
    index = db.Column(db.Integer, unique=True, primary_key=True)
    runid = db.Column(db.String(64))
    pid = db.Column(db.String(64))
    trec = db.Column(db.String(64))
    track = db.Column(db.String(64))
    type = db.Column(db.String(64))
    task = db.Column(db.String(64))
    md5 = db.Column(db.String(64))
    year = db.Column(db.String(64))
    date = db.Column(db.String(64))
    description = db.Column(db.String(64))
    input_url = db.Column(db.String(64))
    summary_url = db.Column(db.String(64))
    appendix_url = db.Column(db.String(64))
    other = db.Column(db.String(64))


    def __repr__(self):
        return f"Run('{self.runid}', '{self.trec}', '{self.track}')" 
    

    def to_json(self):
        json_run = {
            'runid': self.runid,
            'trec': self.trec,
            'type': self.type,
            'task': self.task,
            'track': self.track,
            'md5': self.md5,
            'year': self.year,
            'date': self.date,
            'description': self.description,
            'input_url': self.input_url,
            'summary_url': self.summary_url,
            'appendix_url': self.appendix_url,
            'other': self.other
        }

        for attr in ['summary_url', 'appendix_url', 'other']:
            if json_run.get(attr):
                json_run[attr] = json.loads(json_run[attr]) if is_json(json_run[attr]) else json_run[attr]

        participant = Participant.query.filter(Participant.trec==self.trec, Participant.pid==self.pid).first()
        if participant:
            json_run.update({'participant': participant.to_json()})
            del json_run['participant']['trec']
            del json_run['participant']['year']

        publication = Publication.query.filter(Publication.trec==self.trec, Publication.pid==self.pid).first()
        if publication:
            json_run.update({'publication': publication.to_json()})
            del json_run['publication']['trec']
            del json_run['publication']['track']
            del json_run['publication']['pid']

        dataset = Dataset.query.filter(Dataset.trec==self.trec, Dataset.track==self.track).first()
        if dataset:
            json_run.update({'data': dataset.to_json()})

        results = Result.query.filter(Result.trec==self.trec, Result.track==self.track, Result.runid==self.runid).all()
        evals = set([r.eval for r in results])
        results_dict = dict.fromkeys(evals, dict())
        for eval in evals:
            topics = set([r.topic for r in results])
            res_eval = dict.fromkeys(topics, dict())
            for result in results:
                if result.measure == 'summary':
                    continue
                if result.eval == eval:
                    res_eval[result.topic].update({result.measure: result.score})
            results_dict[eval] = res_eval
        json_run.update({'results': results_dict})
    
        track = Track.query.filter(Track.trec==self.trec, Track.track==self.track).first()
        if track:
            json_run.update({'track': track.to_json()})

        return json_run
    

class Participant(db.Model):
    __tablename__ = 'participants'
    index = db.Column(db.Integer, unique=True, primary_key=True)
    pid = db.Column(db.String(64))
    organization = db.Column(db.String(64))
    name = db.Column(db.String(64))
    trec = db.Column(db.String(64))
    year = db.Column(db.String(64))


    def __repr__(self):
        return f"Participant('{self.pid}', '{self.name}', '{self.trec}')" 


    def to_json(self):
        return {
            'pid': self.pid,
            'organization': self.organization,
            'name': self.name,
            'trec': self.trec,
            'year': self.year
        }


class Dataset(db.Model):
    __tablename__ = 'datasets'
    index = db.Column(db.Integer, unique=True, primary_key=True)
    trec = db.Column(db.String(64))
    track = db.Column(db.String(64))
    corpus = db.Column(db.String(64))
    topics = db.Column(db.String(64))
    qrels = db.Column(db.String(64))
    ir_datasets = db.Column(db.String(64))
    other = db.Column(db.String(64))


    def __repr__(self):
        return f"Dataset('{self.trec}', '{self.track}')" 


    def to_json(self):
        if hasattr(self, 'ir_datasets'):
            ir_datasets = json.loads(self.ir_datasets) if is_json(self.ir_datasets) else self.ir_datasets 
        if hasattr(self, 'corpus'):
            corpus = json.loads(self.corpus) if is_json(self.corpus) else self.corpus  
        if hasattr(self, 'topics'):
            topics = json.loads(self.topics) if is_json(self.topics) else self.topics 
        if hasattr(self, 'qrels'):
            qrels = json.loads(self.qrels) if is_json(self.qrels) else self.qrels 
        if hasattr(self, 'other'):
            other = json.loads(self.other) if is_json(self.other) else self.other 

        return {
            'ir_datasets': ir_datasets,
            'corpus': corpus,
            'topics': topics,
            'qrels': qrels,
            'other': other,
        }


class Publication(db.Model):
    __tablename__ = 'publications'
    index = db.Column(db.Integer, unique=True, primary_key=True)
    trec = db.Column(db.String(64))
    track = db.Column(db.String(64))
    pid = db.Column(db.String(64))
    url = db.Column(db.String(64))
    biburl = db.Column(db.String(64))
    key = db.Column(db.String(64))
    title = db.Column(db.String(64))
    author = db.Column(db.String(64))
    abstract = db.Column(db.String(64))
    bibtex = db.Column(db.String(64))


    def __repr__(self):
        return f"Publication('{self.key}', '{self.pid}', '{self.trec}', '{self.track}')"  
    

    def to_json(self):
        return {
            'trec': self.trec,
            'track': self.track,
            'pid': self.pid,
            'url': self.url,
            'biburl': self.biburl,
            'key': self.key,
            'title': self.title,
            'author': self.author,
            'abstract': self.abstract,
            'bibtex': self.bibtex
        }


class Result(db.Model):
    __tablename__ = 'results'
    index = db.Column(db.Integer, unique=True, primary_key=True)
    trec = db.Column(db.String(64))
    track = db.Column(db.String(64))
    runid = db.Column(db.String(64))
    eval = db.Column(db.String(64))
    measure = db.Column(db.String(64))
    topic = db.Column(db.String(64))
    score = db.Column(db.String(64))


    def __repr__(self):
        return f"Result('{self.trec}', '{self.track}', '{self.runid}', '{self.measure}')"   
    

    def to_json(self):
        return {
            'trec': self.trec,
            'track': self.track,
            'runid': self.runid,
            'eval': self.eval,
            'measure': self.measure,
            'topic': self.topic,
            'score': self.score
        }


class Track(db.Model):
    __tablename__ = 'tracks'
    index = db.Column(db.Integer, unique=True, primary_key=True)
    trec = db.Column(db.String(64))
    track = db.Column(db.String(64))
    fullname = db.Column(db.String(64))
    tasks = db.Column(db.String(64))
    webpage = db.Column(db.String(64))
    coordinators = db.Column(db.String(64))
    description = db.Column(db.String(64))


    def __repr__(self):
        return f"Track('{self.trec}', '{self.track}', '{self.fullname}')"   


    def to_json(self):
        return {
            'trec': self.trec,
            'trackid': self.track,
            'fullname': self.fullname,
            'tasks': json.loads(self.tasks) if is_json(self.tasks) else self.tasks, 
            'webpage': self.webpage,
            'coordinators': self.coordinators.split(':'),
            'description': self.description
        }
