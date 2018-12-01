#!/bin/bash
# elecsecrun

# Stop on errors, print on commands
set -e
set -x

# Set FLASK_DEBUG, FLASK_APP, INSTA485_SETTINGS
export FLASK_DEBUG=True
export FLASK_APP=elecsec

# Run development server on port 8000
flask run --host 0.0.0.0 --port 8000