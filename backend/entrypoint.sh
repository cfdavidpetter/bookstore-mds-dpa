#!/bin/sh

if [ ! -d "venv" ]; then
  python3 -m venv venv
  ./venv/bin/pip install --upgrade pip
  ./venv/bin/pip install -r requirements.txt
fi

exec ./venv/bin/flask --app app run --host=0.0.0.0
