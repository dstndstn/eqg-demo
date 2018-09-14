#! /bin/bash

export PYTHONPATH=${PYTHONPATH}:.

uwsgi -s :5000 --wsgi-file wsgi.py --touch-reload wsgi.py --processes 8 -d uwsgi.log 



