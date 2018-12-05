"""Elecsec development configuration."""

import os

APPLICATION_ROOT = '/'

SECRET_KEY = os.environ.get('SECRET_KEY') or 'alex-halderman'

AUDIT_FILENAME = os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
    'audit.py'
)