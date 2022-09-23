#!/usr/bin/python3
import requests
from sys import argv
"""
Module: 2-post_email.py
"""

if __name__ == "__main__":
    data = {'email': argv[2]}
    r = requests.get(argv[1])
    print(r.text)
