#!/usr/bin/python3
from urllib import request
"""
Module: 0-hbtn_status.py
"""

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    with request.urlopen(url) as resp:
        print(f"Body response:\n\t- type: {resp.peek().__class__}",
              f"\n\t- content: {resp.read()}\n\t- utf8 content: {resp.reason}")
