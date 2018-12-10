"""Elecsec package initializer."""

import flask

app = flask.Flask(__name__)
app.config.from_object('elecsec_web.config')

import elecsec_web.views
import elecsec_web.model