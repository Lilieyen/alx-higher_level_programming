#!/bin/bash
#send GET request and header must be sent withthe value 98
curl -sX GET -H "X-HolbertonSchool-User-Id: 98" "$1"
