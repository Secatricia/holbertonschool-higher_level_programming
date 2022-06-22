#!/usr/bin/python3
"""
Takes in a letter and sends a POST request to 8-json_api.py
with the letter as a parameter.
"""
import requests
import sys
if __name__ == "__main__":

    dt = "" if len(sys.argv) == 1 else sys.argv[1]
    re = requests.post('http://0.0.0.0:5000/search_user', data={'q': dt})

    try:
        resp = re.json()
        if resp == {}:
            print('No result')
        else:
            print("[{}] {}".format(resp.get('id'), resp.get('name')))
    except ValueError:
        print('Not a valid JSON')
