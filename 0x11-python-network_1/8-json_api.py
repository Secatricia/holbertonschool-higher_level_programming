#!/usr/bin/python3
"""
Takes in a letter and sends a POST request to 8-json_api.py
with the letter as a parameter.
"""
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) == 1:
        dt = {'q': ""}
    else:
        dt = {'q': argv[1]}

    response = requests.post(url='http://0.0.0.0:5000/search_user', data=dt)
    re = response.json()
    if response.headers.get('content-type') != 'application/json':
        print('Not a valid JSON')
    elif re == {}:
        print('No result')
    else:
        print('[{}] {}'.format(re['id'], re['name']))
