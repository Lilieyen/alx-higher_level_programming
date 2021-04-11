#!/bin/bash
#sends a JSON POST request to a URL passed as the first argument & filename as second arg
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
