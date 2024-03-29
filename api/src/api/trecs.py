from flask import jsonify
from . import api
from main import app
from models import Run


# get all trec conferences
@api.route('/trecs')
def get_trecs():

    with app.app_context():

        distinct_trecs = Run.query.with_entities(Run.trec).distinct() 
        distinct_trecs = [r.trec for r in distinct_trecs]

        return jsonify(distinct_trecs)
