#!/usr/bin/python3
"""
Module: 0-hbtn_status.py
"""

from urllib import request


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    with request.urlopen(url) as r:
        data = r.read()
        print(f"Body response:\n\t- type:{data.__class__}\n\t- content: {data}",
              f"\n\t- utf8 content: {data.decode('utf-8')}")
