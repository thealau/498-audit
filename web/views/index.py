"""Flask app for audit program."""
import json
import requests
import elecsec
import flask
from flask import request
from subprocess import Popen, PIPE, STDOUT


@elecsec.app.route('/')
def show_audit():
    """Get results of audit query."""
    state_csvs_dict = {};
    state_csvs_dict["Michigan"] = "20161108__mi__general__precinct.csv"
    state = request.args.get('state')
    mode = request.args.get('mode')
    col = request.args.get('col')
    race = request.args.get('race')
    percent = request.args.get('percent')
    if all(v is not None for v in [query, weight]):
        # get state file from dictionary
        state_csv = state_csvs_dict[state]
        # pass state file to audit.py
        p = Popen(['audit.py', state_csv], stdout=PIPE, stdin=PIPE, stderr=STDOUT)    
        # pass rest of options
        audit_stdout = p.communicate(input=mode)[0]
        audit_stdout = p.communicate(input=col)[0]
        audit_stdout = p.communicate(input=race)[0]
        audit_stdout = p.communicate(input=percent)[0]
        context = audit_stdout.decode()

        return flask.render_template("index.html", context=context)
    return flask.render_template("index.html")
