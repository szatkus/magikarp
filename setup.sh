#!/bin/bash

if [ ! -f config.py ]; then
  echo "config.py not found"
  exit
fi

python3 -m venv venv
venv/bin/pip install -r requirements.txt
echo -e "from database import db\ndb.create_all()\nimport testdata" | venv/bin/python

echo
echo "Run "venv/bin/python main.py" to start."
