#!/bin/bash
#bash script that takes in a URL, sends a request and displays size of response
curl -sI "$1" | grep 'Content-Length:' | cut -d' ' -f2
