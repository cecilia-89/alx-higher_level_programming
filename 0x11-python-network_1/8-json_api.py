#!/usr/bin/python3
"""
Module: 8-json_api.py
"""
import requests
from sys import argv


if __name__ == "__main__":

    value = ""
    if len(argv) > 1:
        value = argv[1]
    data = {'q': value}
    r = requests.post("http://0.0.0.0:5000/search_user", data=data)
    try:
        js = r.json()
        if js.__len__() == 0:
            print("No result")
        else:
            print(f"[{js.get('id')}]", js.get('name'))
    except ValueError:
        print("Not a valid JSON")
