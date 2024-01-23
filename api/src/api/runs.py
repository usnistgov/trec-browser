from flask import jsonify
from . import api
from main import app
from models import Run


# get all run (names) of a specified track of a specified trec conference
@api.route('/<string:trec>/<string:track>/runs')
def get_track_runs(trec, track):
    
    with app.app_context():

        _runs = Run.query.filter(
            Run.trec==trec, 
            Run.track==track
            ).all()
        
        if _runs:
            runs = [r.to_json() for r in _runs]
    
            return jsonify(runs)
        
    return jsonify([])


# get all runs from a specified participant at a specified track
@api.route('/<string:trec>/<string:track>/<string:pid>/runs')
def get_participant_runs(trec, track, pid):

    with app.app_context():

        _runs = Run.query.filter(
            Run.trec==trec, 
            Run.track==track, 
            Run.pid==pid
            ).all()
        
        if _runs:
            runs = [r.to_json() for r in _runs]
    
            return jsonify(runs)
        
    return jsonify([])


# get the run with specified runid
@api.route('/<string:trec>/<string:track>/<string:pid>/<string:runid>')
def get_run(trec, track, pid, runid):

    with app.app_context():

        r = Run.query.filter(
            Run.trec==trec, 
            Run.track==track, 
            Run.pid==pid, 
            Run.runid==runid
            ).first()
        
        if r:
            resp = r.to_json()
            return jsonify(resp)
    
    return jsonify([])


# get all the runs with the specified runid (includes multiple tracks)
@api.route('/runs/<string:runid>')
def get_runs(runid):
    
    with app.app_context():

        _runs = Run.query.filter(Run.runid==runid).all()
        
        if _runs:
            runs = [r.to_json() for r in _runs]
    
            return jsonify(runs)
        
    return jsonify([])


# get all runs from a specified participant 
@api.route('/<string:pid>/runs/')
def get_all_participant_runs(pid):

    with app.app_context():

        _runs = Run.query.filter(Run.pid==pid).all()
        
        if _runs:
            runs = [r.to_json() for r in _runs]
    
            return jsonify(runs)
        
    return jsonify([])
    