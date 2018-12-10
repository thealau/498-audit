"""Flask app for audit program."""
import json
import elecsec_web
import flask
from flask import request
from subprocess import Popen, PIPE, STDOUT


@elecsec_web.app.route('/')
def show_index():
    """Get results of audit query."""
    if(request.args.get('btn') == "search"):
        context = {}
        state_data = elecsec_web.model.query_db(
                "SELECT * from policies where \
            state = ?", [request.args.get('state_audit')], one=True)
        context['state'] = request.args.get('state_audit')
        context['policy'] = state_data['policy']
        context['autoprob'] = state_data['prob']
        return flask.render_template("index.html", context=context)

    if(request.args.get('btn') == "calculate"):
        state_csvs_dict = {};
        state_csvs_dict["Arkansas"] = "20161108__ak__general__precinct.csv"
        state_csvs_dict["California"] = "2016_precinct_california.csv"
        state_csvs_dict["Connecticut"] = "20161108__ct__general__precinct.csv"
        state_csvs_dict["District of Columbia"] = "20161108__dc__general__precinct.csv"
        state_csvs_dict["Hawaii"] = "20161108__hi__general__precinct.csv"
        state_csvs_dict["Illinois"] = "20161108__il__general__precinct.csv"
        state_csvs_dict["Iowa"] = "20161108__ia__general__precinct.csv"
        state_csvs_dict["Massachusetts"] = "20161108__ma__general__precinct.csv"
        state_csvs_dict["Michigan"] = "20161108__mi__general__precinct.csv"
        state_csvs_dict["Minnesota"] = "20161108__mn__general__precinct.csv"
        state_csvs_dict["Missouri"] = "20161108__mo__general__precinct.csv"
        state_csvs_dict["Montana"] = "20161108__mt__general__precinct.csv"
        state_csvs_dict["Nebraska"] = "20161108__ne__general__precinct.csv"
        state_csvs_dict["Nevada"] = "20161108__nv__general__county.csv"
        state_csvs_dict["New York"] = "20161108__ny__general.csv"
        state_csvs_dict["Ohio"] = "20161108__oh__general.csv"
        state_csvs_dict["Oregon"] = "20161108__or__general__precinct.csv"
        state_csvs_dict["Pennsylvania"] = "20161108__pa__general__precinct.csv"
        state_csvs_dict["Texas"] = "20161108__tx__general__county.csv"
        state_csvs_dict["Utah"] = "20161108__ut__general__county.csv"
        state_csvs_dict["Vermont"] = "20161108__vt__general__precinct.csv"
        state_csvs_dict["Washington"] = "20161108__wa__general__county.csv"
        state_csvs_dict["Wisconsin"] = "20161108__wi__general__ward.csv"
        state = request.args.get('state')
        audit_type = request.args.get('audit_type')
        col = request.args.get('col')
        race = request.args.get('race')
        percent = request.args.get('percent')
        msg = str.encode(audit_type + ',' + col + ',' + race + ',' + percent)
        if all(v is not None for v in [audit_type, col, race, percent]):
            # get state file from dictionary
            state_csv = state_csvs_dict[state]
            # pass state file to audit.py
            p = Popen([elecsec_web.app.config['AUDIT_FILENAME'], "-m", "web", state_csv], stdout=PIPE, stdin=PIPE, stderr=STDOUT)    
            # pass rest of options
            audit_stdout = p.communicate(input=msg)[0]
            context = {}
            context['state'] = request.args.get('state')
            context['audit_type'] = request.args.get('audit_type')
            context['col'] = request.args.get('col')
            context['race'] = request.args.get('race')
            context['percent'] = request.args.get('percent')
            context['prob'] = audit_stdout.decode()

            return flask.render_template("index.html", context=context)
    return flask.render_template("index.html")
