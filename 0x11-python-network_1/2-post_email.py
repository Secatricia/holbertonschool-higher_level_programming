#!/usr/bin/python3
"""takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter"""

if __name__ == "__main__":
    import urllib.request
    from sys import argv

    with urllib.request.urlopen(argv[1]) as r:
        name = r.name()
        content = name.get('X-Request-Id')
        print(content)
