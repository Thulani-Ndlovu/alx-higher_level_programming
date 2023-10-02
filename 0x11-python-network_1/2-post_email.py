#!/usr/bin/python3
'''
    Python script that takes in a URL and an email,
    sends a POST request to the passed URL with
    the email as a parameter,
    and displays the body of the response (decoded in utf-8)
'''
import urllib.request
import urllib.parse
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    val = {"email": sys.argv[2]}
    info = urllib.parse.urlencode(val).encode("ascii")

    req = urllib.request.Request(url, info)
    with urllib.request.urlopen(req) as res:
        print(res.read().decode("utf-8"))
