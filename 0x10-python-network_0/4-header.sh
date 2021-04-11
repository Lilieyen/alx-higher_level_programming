#!/bin/bash
#send GET request and header must be sent withthe value 98
curl -sX GET "$1" -H "X-HolbertonSchool-User-Id=98"
