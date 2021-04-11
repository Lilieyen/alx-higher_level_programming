#!/bin/bash
#sends a DELETE request to the URL (1st arg) & display the body of the response
curl -sX DELETE "$1"
