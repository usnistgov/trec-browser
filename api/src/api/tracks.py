from flask import jsonify
from . import api
from main import app
from models import Track, Run, no_tracks


@api.route('/<string:trec>/tracks')
def get_tracks(trec):
    # get all tracks of a TREC conference

    with app.app_context():
        _tracks = Track.query.filter(Track.trec==trec).all()

        if _tracks:
            tracks = [t.to_json() for t in _tracks]
            tracks = filter(lambda x: x.get('track') not in no_tracks, tracks)

            return jsonify(list(tracks))

        return jsonify([])


@api.route('/<string:trec>/<string:pid>/tracks')
def get_participant_tracks(trec, pid):
    # get all tracks in which the participant participated in a specified conference

    with app.app_context():

        _distinct_tracks = Run.query.filter(
            Run.trec==trec,
            Run.pid==pid
            ).with_entities(Run.track).distinct()
        
        if _distinct_tracks:

            tracks = [r.track for r in _distinct_tracks]
            tracks = filter(lambda x: x not in no_tracks, tracks)

            # return jsonify({trec: list(tracks)})
            return jsonify(list(tracks))        
                

        return jsonify([])
