from flask import jsonify
from . import api
from main import app
from models import Publication, Run


# get all publications of a track
@api.route('/<string:trec>/<string:track>/publications')
def get_track_publications(trec, track):
    
    with app.app_context():

        _publications = Publication.query.filter(
            Publication.trec==trec, 
            Publication.track==track
            ).all()
        
        if _publications:
            _publications = [p.to_json() for p in _publications]

            for p in _publications:
    
                _runids = Run.query.filter(
                    Run.trec==trec, 
                    Run.track==track,
                    Run.pid==p['pid']
                    ).with_entities(Run.runid).distinct()
                
                runids = [r.runid for r in _runids]

                if len(runids):
                    p.update({'runids': runids})
            
            return jsonify(_publications)
        
    return jsonify([])


# get all publications of a trec conference
@api.route('/<string:trec>/publications')
def get_trec_publications(trec):
    
    with app.app_context():

        _distinct_tracks = Publication.query.filter(
            Publication.trec==trec
            ).with_entities(Publication.track).distinct()
        
        distinct_tracks = [t.track for t in _distinct_tracks]
 
        _publications = Publication.query.filter(
            Publication.trec==trec
            ).all()
        
        if _publications:

            response = {}

            for track in distinct_tracks:

                _track_publications = filter(lambda x: x.track == track, _publications)
    
                track_publications = [r.to_json() for r in _track_publications]

                for p in track_publications:
    
                    _runids = Run.query.filter(
                        Run.trec==trec, 
                        Run.track==track,
                        Run.pid==p['pid']
                        ).with_entities(Run.runid).distinct()
                    
                    runids = [r.runid for r in _runids]

                    if len(runids):
                        p.update({'runids': runids})

                response[track] = track_publications

            return jsonify(response)
        
    return jsonify([])
