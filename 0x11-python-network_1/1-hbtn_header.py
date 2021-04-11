#!/usr/bin/python3
"""send a request to the URL & display value of var found in header response"""
import urllib.request as request
from sys import argv

if __name__ == "__main__":
    req = request.Request(argv[1])
    with request.urlopen(req) as r:
        print(r.headers.get('X-Request-Id'))
