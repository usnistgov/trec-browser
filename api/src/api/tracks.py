from flask import jsonify
from . import api
from main import app
from models import Track, Run


# get all tracks of a TREC conference
@api.route('/<string:trec>/tracks')
def get_tracks(trec):

    with app.app_context():
        _tracks = Track.query.filter(Track.trec==trec).all()

        if _tracks:
            tracks = [t.to_json() for t in _tracks]

            return jsonify(list(tracks))

        return jsonify([])


# get all tracks in which the participant participated in a specified conference
@api.route('/<string:trec>/<string:pid>/tracks')
def get_participant_tracks(trec, pid):

    with app.app_context():

        _distinct_tracks = Run.query.filter(
            Run.trec==trec,
            Run.pid==pid
            ).with_entities(Run.track).distinct()
        
        if _distinct_tracks:

            tracks = [r.track for r in _distinct_tracks]

            return jsonify(list(tracks))        
                

        return jsonify([])
