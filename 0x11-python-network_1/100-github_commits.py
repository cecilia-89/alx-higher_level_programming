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
    length = len(js)
    if length > 10:
        length = 10
    for i in range(length):
        author = js[i].get('commit').get('author')
        print(js[i].get('sha') + ':', author.get('name'))
