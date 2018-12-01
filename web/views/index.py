"""Flask app for search server."""
import json
import search
import requests
import flask
from flask import request
from subprocess import Popen, PIPE, STDOUT


@search.app.route('/')
def show_audit():
    """Get results of audit query."""
    state = request.args.get('state')
    mode = request.args.get('mode')
    col = request.args.get('col')
    race = request.args.get('race')
    percent = request.args.get('percent')
    if all(v is not None for v in [query, weight]):
        # get state file from dictionary
        # pass state file to audit.py
        # pass rest of options


        return flask.render_template("index.html", context=context)
    return flask.render_template("index.html")
