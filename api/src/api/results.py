from flask import jsonify
from . import api
from main import app
from models import Run, Result


@api.route('/<string:trec>/<string:track>/results')
def get_track_results(trec, track):
    # get all results of a track
    
    with app.app_context():

        results_json = {}

        _pids = Run.query.filter(
            Run.trec==trec, 
            Run.track==track
            ).with_entities(Run.pid).distinct()
        
        pids = [p.pid for p in _pids]

        for pid in pids:

            p_results = {}

            _runs = Run.query.filter(
                Run.trec==trec, 
                Run.track==track,
                Run.pid==pid
                ).all()
            
            if _runs:

                for r in _runs:

                    results = Result.query.filter(Result.trec==trec, Result.track==track, Result.runid==r.runid).all()

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

                    p_results[r.runid] = _res_eval

            results_json[pid] = p_results
        
        return jsonify(results_json)
        
    return jsonify([])


@api.route('/<string:trec>/<string:track>/<string:pid>/results')
def get_participant_results(trec, track, pid):
    # get all results of a trec conference

    with app.app_context():    
        results_json = {}

        _runs = Run.query.filter(
            Run.trec==trec, 
            Run.track==track,
            Run.pid==pid
            ).all()
        
        if _runs:

            for r in _runs:

                results = Result.query.filter(Result.trec==trec, Result.track==track, Result.runid==r.runid).all()

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

                results_json[r.runid] = _res_eval

            return jsonify(results_json)
        
    return jsonify([])
