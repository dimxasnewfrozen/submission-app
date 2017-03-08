#!/bin/bash

# Start Gunicorn processes
echo Starting Gunicorn.
exec gunicorn submissions_app.wsgi:application \
    --bind 127.0.0.1:3000 \
    --workers 5