#!/usr/bin/python3
"""takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter"""

import sys
import urllib.request


if __name__ == "__main__":
    data = urllib.parse.urlencode({"email": sys.argv[2]}).encode('utf-8')

    req = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(req) as response:
        html = response.read()

    print(html.decode('utf-8'))
