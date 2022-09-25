#!/usr/bin/python3
"""
Module: 10-my_github.py
"""
import requests
from sys import argv

if __name__ == "__main__":

    r = requests.get(f"https://api.github.com/repos/{argv[2]}/{argv[1]}/commits",)
    js = r.json()
    for i in range(10):
        author = js[i].get('commit').get('author')
        print(js[i].get('sha') + ':', author.get('name') )
