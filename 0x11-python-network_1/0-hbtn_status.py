#!/usr/bin/python3
"""
Module: 0-hbtn_status.py
"""

from urllib import request


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    with request.urlopen(url) as r:
        print(f"Body response:\n\t- type:{r.peek().__class__}\
              \n\t- content: {r.read()}\
              \n\t- utf8 content: {r.reason}".expandtabs(4))
