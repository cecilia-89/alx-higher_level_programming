#!/usr/bin/python3
"""
Module: 10-my_github.py
"""
import requests
from sys import argv

pat = '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'
if __name__ == "__main__":

    r = requests.get("https://api.github.com/user", auth=(argv[1], argv[2]))
    js = r.json()
    print(js.get('id'))
