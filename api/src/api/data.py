from flask import jsonify
from . import api
from main import app
from models import Dataset


@api.route('/<string:trec>/<string:track>/data')
def get_track_data(trec, track):
    # get data of a track

    with app.app_context():    

        dataset = Dataset.query.filter(
            Dataset.trec==trec, 
            Dataset.track==track
            ).first()
    
        if dataset:
            return jsonify(dataset.to_json())

    return jsonify([])


@api.route('/<string:trec>/data')
def get_trec_data(trec):
    # get all data of a trec conference
        
    with app.app_context(): 

        datasets_json = {}

        _tracks = Dataset.query.filter(
            Dataset.trec==trec
            ).with_entities(Dataset.track).distinct() 

        tracks = [d.track for d in _tracks]

        for track in tracks:

            dataset = Dataset.query.filter(
                Dataset.trec==trec,
                Dataset.track==track
                ).first()
    
            if dataset:
                datasets_json[track] = dataset.to_json()

        return jsonify(datasets_json)

