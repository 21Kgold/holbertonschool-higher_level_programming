#!/usr/bin/python3
"""
Script that takes your GitHub credentials (username and password) and uses the
GitHub API to display your id.  You must use Basic Authentication with a
personal access token as password to access to your information (only read:user
permission is needed)
"""

import requests
import sys

if __name__ == "__main__":
    usr = sys.rgv[1]
    pwd = sys.argv[2]
    response = requests.get('https://api.github.com/user', auth=(usr, pwd))
    json_response = response.json()
    try:
        print("{}".format(json_response.get('id')))
    except keyError:
        print("None")
