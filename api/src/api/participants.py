from flask import jsonify
from . import api
from main import app
from models import Participant, Run


# get all participants of a track
@api.route('/<string:trec>/<string:track>/participants')
def get_track_participants(trec, track):
    
    with app.app_context():

        _distinct_pids = Run.query.filter(
            Run.trec==trec, 
            Run.track==track
            ).with_entities(Run.pid).distinct()
        
        distinct_pids = [pid.pid for pid in _distinct_pids]
 
        _participants = Participant.query.filter(
            Participant.trec==trec
            ).all()
        
        if _participants:
            _participants = filter(lambda x: x.pid in distinct_pids, _participants)
            participants = [r.to_json() for r in _participants]
            for r in participants:
                r.update({'track': track}) 

            return jsonify(participants)
        
    return jsonify([])


# get all participants of a trec conference
@api.route('/<string:trec>/participants')
def get_trec_participants(trec):
    
    with app.app_context():

        _distinct_pids = Run.query.filter(
            Run.trec==trec
            ).with_entities(Run.pid).distinct()
        
        distinct_pids = [pid.pid for pid in _distinct_pids]
 
        _participants = Participant.query.filter(
            Participant.trec==trec
            ).all()
        
        if _participants:
            _participants = filter(lambda x: x.pid in distinct_pids, _participants)
    
            participants = [r.to_json() for r in _participants]

            for p in participants:
                _distinct_tracks_runs = Run.query.filter(
                    Run.pid==p.get('pid'),
                    Run.trec==trec, 
                    ).with_entities(Run.track).distinct()
                p['tracks'] = [run.track for run in _distinct_tracks_runs]

            participants = filter(lambda x: len(x.get('tracks')) > 0, participants)

            return jsonify(list(participants))
        
    return jsonify([])
