#!/bin/bash
# Run the transcript fetcher using the virtual environment

if [ -z "$1" ]; then
    echo "Usage: ./run.sh <youtube_url>"
    exit 1
fi

venv/bin/python get_transcript.py "$@"
