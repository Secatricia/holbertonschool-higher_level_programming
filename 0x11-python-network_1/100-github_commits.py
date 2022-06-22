#!/usr/bin/python3
"""script that takes 2 arguments in order to solve this challenge
"""
import sys
import requests


if __name__ == "__main__":
    re = requests.get('https://api.github.com/repos/{}/{}/commits'
                      .format(sys.argv[2], sys.argv[1]))
    if re.status_code >= 400:
        print('None')
    else:
        for comment in re.json()[:10]:
            print("{}: {}".format(comment.get('sha'),
                                  comment.get('commit').get('author')
                                         .get('name')))
