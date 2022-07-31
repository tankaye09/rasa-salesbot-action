#!/bin/sh

if [ -z "$PORT"]
then
  PORT=5055
fi

# rasa run --enable-api --port $PORT
# rasa run actions -p $PORT
python -m rasa_sdk --actions actions -p $PORT