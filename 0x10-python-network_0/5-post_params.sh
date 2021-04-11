#!/bin/bash
#sends a POST request to the passed URL, and has an email an subject var
curl -sX POST -d {"email": "hr@holbertonschool.com", "subject": "I will always be here for PLD"} "$1"
