#!/usr/bin/python3
"""
Module: 10-my_github.py
"""
import requests
from sys import argv

if __name__ == "__main__":

    r = requests.get("https://api.github.com/repos/"
                     f"{argv[2]}/{argv[1]}/commits")
    js = r.json()
    for commit in js[:10]:
        author = commit.get('commit').get('author').get('name')
        print(commit.get('sha') + ':', author)
