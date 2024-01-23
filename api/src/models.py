from main import db
import json


def is_json(json_data):
    try:
        json.loads(json_data)
    except ValueError as err:
        return False
    return True


class Run(db.Model):

    __tablename__ = 'runs'

    index = db.Column(db.Integer, unique=True, primary_key=True)
    runid = db.Column(db.String(64))
    trec = db.Column(db.String(64))
    track = db.Column(db.String(64))
    pid = db.Column(db.String(64))
    year = db.Column(db.String(64))
    date = db.Column(db.String(64))
    type = db.Column(db.String(64))
    task = db.Column(db.String(64))
    track = db.Column(db.String(64))
    md5 = db.Column(db.String(64))
    description = db.Column(db.String(64))
    repository = db.Column(db.String(64))
    hardware = db.Column(db.String(64))
    summary_url = db.Column(db.String(64))
    input_url = db.Column(db.String(64))
    appendix_url = db.Column(db.String(64))


    def __repr__(self):
        return f"Run('{self.runid}', '{self.trec}', '{self.track}')" 
    

    def to_json(self):

        json_run = {
            'runid': self.runid,
            'trec': self.trec,
            'track': self.track,
            'type': self.type,
            'task': self.task,
            'track': self.track,
            'md5': self.md5,
            'year': self.year,
            'date': self.date,
            'description': self.description,
            'repository': self.repository,
            'hardware': self.hardware,
            'input_url': self.input_url,
            'summary_url': self.summary_url,
            'appendix_url': self.appendix_url
        }

        participant = Participant.query.filter(Participant.trec==self.trec, Participant.pid==self.pid).first()

        if participant:
            organization =  participant.organization
            name =  participant.name

            json_run.update(
                {
                    'participant': {
                        'name': name,
                        'organization': organization,
                        'pid': self.pid,
                    }
                }
            )

        publication = Publication.query.filter(Publication.trec==self.trec, Publication.pid==self.pid).first()
        if publication:
            puburl = publication.url
            biburl =  publication.biburl
            pubkey = publication.key
            pubtitle = publication.title
            pubauthor = publication.author
            pubbibtex = publication.bibtex

            json_run.update(
                {
                    'publication': {
                        'url': puburl,
                        'biburl': biburl,
                        'key': pubkey, 
                        'title': pubtitle,
                        'author': pubauthor,
                        'bibtex': pubbibtex
                    }
                }
            )

        dataset = Dataset.query.filter(Dataset.trec==self.trec, Dataset.track==self.track).first()

        if dataset:
            if hasattr(dataset, 'ir_datasets'):
                ir_datasets = json.loads(dataset.ir_datasets) if is_json(dataset.ir_datasets) else dataset.ir_datasets 
            if hasattr(dataset, 'corpus'):
                corpus = json.loads(dataset.corpus) if is_json(dataset.corpus) else dataset.corpus  
            if hasattr(dataset, 'topics'):
                topics = json.loads(dataset.topics) if is_json(dataset.topics) else dataset.topics 
            if hasattr(dataset, 'qrels'):
                qrels = json.loads(dataset.qrels) if is_json(dataset.qrels) else dataset.qrels 
            if hasattr(dataset, 'other'):
                if dataset.other:
                    if is_json(dataset.other):
                        other = json.loads(dataset.other)
                else:
                    other = dataset.other
            else:
                other = dataset.other

            json_run.update(
                {
                    'data':{
                        'ir_datasets': ir_datasets,
                        'corpus': corpus if corpus else '',
                        'topics': topics if topics else '',
                        'qrels': qrels if qrels else '',
                        'other': other if other else '',
                    }
                }
            )

        results = Result.query.filter(Result.trec==self.trec, Result.track==self.track, Result.runid==self.runid).all()

        evals = set([r.eval for r in results])
        _res = dict.fromkeys(evals, dict())

        for eval in evals:

            topics = set([r.topic for r in results])
            _res_eval = dict.fromkeys(topics, dict())

            for result in results:

                if result.measure == 'summary':
                    continue

                if result.eval == eval:

                    _res_eval[result.topic].update(
                    {
                        result.measure: result.score
                    }
                )
                
            _res[eval] = _res_eval


        json_run.update(
            {
                'results': _res
            }
        )

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
        json_participant = {
            'pid': self.pid,
            'organization': self.organization,
            'name': self.name,
            'trec': self.trec,
            'year': self.year
        }

        return json_participant


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
            if self.other:
                if is_json(self.other):
                    other = json.loads(self.other)
            else:
                other = self.other
        else:
            other = self.other

        return {
            'ir_datasets': ir_datasets,
            'corpus': corpus if corpus else '',
            'topics': topics if topics else '',
            'qrels': qrels if qrels else '',
            'other': other if other else '',
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
    bibtex = db.Column(db.String(64))


    def __repr__(self):
        return f"Publication('{self.key}', '{self.pid}', '{self.trec}', '{self.track}')"  
    

    def to_json(self):
        json_publication = {
            'trec': self.trec,
            'track': self.track,
            'pid': self.pid,
            'url': self.url,
            'biburl': self.biburl,
            'key': self.key,
            'title': self.title,
            'author': self.author,
            'bibtex': self.bibtex
        }

        return json_publication


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
        json_publication = {
            'trec': self.trec,
            'track': self.track,
            'runid': self.runid,
            'eval': self.eval,
            'measure': self.measure,
            'topic': self.topic,
            'score': self.score
        }

        return json_publication


class Track(db.Model):

    __tablename__ = 'tracks'

    index = db.Column(db.Integer, unique=True, primary_key=True)
    trec = db.Column(db.String(64))
    track = db.Column(db.String(64))
    fullname = db.Column(db.String(64))


    def __repr__(self):
        return f"Track('{self.trec}', '{self.track}', '{self.fullname}')"   


    def to_json(self):
        json_track = {
            'trec': self.trec,
            'track': self.track,
            'fullname': self.fullname
        }

        return json_track
