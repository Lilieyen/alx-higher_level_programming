#!/bin/bash
#send GET request and header must be sent withthe value 98
curl -sX "$1" GET -H "X-HolbertonSchool-User-Id: 98" 
