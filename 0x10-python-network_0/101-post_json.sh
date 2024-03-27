#!/bin/bash
# Send a JSON POST request to a URL first argument, displays the Response
curl -sX POST -d "@$2" -H "Content-Type: application/json" "$1"
