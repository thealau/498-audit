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
        context['prob'] = state_data['prob']
        return flask.render_template("index.html", context=context)

    if(request.args.get('btn') == "calculate"):
        state_csvs_dict = {};
        state_csvs_dict["Michigan"] = "20161108__mi__general__precinct.csv"
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
