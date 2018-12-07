#!/bin/bash
# insta485db

# Stop on errors
set -e

# Sanity check command line options
usage() {
  echo "Usage: $0 (create|destroy|reset)"
}

if [ $# -ne 1 ]; then
  usage
  exit 1
fi

# Parse argument.  $1 is the first argument
case $1 in
  "create")
    # echo "FIXME implement me"
    sqlite3 var/elecsec_web.sqlite3 < sql/schema.sql
    echo "+ sqlite3 var/elecsec_web.sqlite3 < sql/schema.sql"
    sqlite3 var/elecsec_web.sqlite3 < sql/data.sql
    echo "+ sqlite3 var/elecsec_web.sqlite3 < sql/data.sql"
    ;;

  "destroy")
    # echo "FIXME implement me"
    rm -rf var/elecsec_web.sqlite3
    echo "+ rm -rf var/elecsec_web.sqlite3 "
    ;;

  "reset")
    # echo "FIXME implement me"
    rm -rf var/elecsec_web.sqlite3
    echo "+ rm -rf var/elecsec_web.sqlite3"
    sqlite3 var/elecsec_web.sqlite3 < sql/schema.sql
    echo "+ sqlite3 var/elecsec_web.sqlite3 < sql/schema.sql"
    sqlite3 var/elecsec_web.sqlite3 < sql/data.sql
    echo "+ sqlite3 var/elecsec_web.sqlite3 < sql/data.sql"
    ;;

  *)
    usage
    exit 1
    ;;
esac