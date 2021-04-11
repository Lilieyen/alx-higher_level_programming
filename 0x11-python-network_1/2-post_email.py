#!/usr/bin/python3
"""
script that takes in a URL and an email, sends a POST request to the passed URL
with the email as a parameter, and displays the body of the response
(decoded in utf-8)
"""
from sys import argv
import urllib.request as request
import urllib.parse as parse

if __name__ == "__main__":
    values = {'email': argv[2]}
    data = parse.urlencode(values).encode('utf-8')
    req = request.Request(argv[1], data)
    with request.urlopen(req) as r:
        print(r.read().decode('utf-8'))
