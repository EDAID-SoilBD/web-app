#!/usr/bin/env bash

echo "Killing all Python processes"
pkill -9 python

echo "Launching backend REST API"
python3 ./backend/main.py&

echo "Launching Web-app"
python3 ./frontend/main.py&

google-chrome "http://localhost:4000"&
