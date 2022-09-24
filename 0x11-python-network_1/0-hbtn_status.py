#!/usr/bin/python3
"""
Module: 0-hbtn_status.py
"""

from urllib import request


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    with request.urlopen(url) as r:
        data = r.read()
        print(f"Body response:\n- type:{data.__class__}\n- content: {data}\
              \n- utf8 content: {data.decode('utf-8')}")
