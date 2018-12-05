"""Elecsec development configuration."""

import os

APPLICATION_ROOT = '/'

SECRET_KEY = os.environ.get('SECRET_KEY') or 'alex-halderman'

# Database file is var/insta485.sqlite3
DATABASE_FILENAME = os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
    'var', 'elecsec.sqlite3'
)

AUDIT_FILENAME = os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
    'audit.py'
)