#!/usr/bin/python3
"""takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter"""

from requests import request


if __name__ == "__main__":
    import urllib.request
    from sys import argv

    val = {'email': argv[2]}
    content = urllib.parse.urlencode(val).encode('ascii')
    req = urllib.request.Request(argv[1], data=content, method='POST')
    with urllib.request.urlopen(req) as n:
        readed = n.read().decode('utf-8')
        print(readed)
