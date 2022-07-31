#!/bin/sh

if [ -z "$PORT"]
then
  PORT=5055
fi

# rasa run --enable-api --port $PORT
start --actions actions -p $PORT
