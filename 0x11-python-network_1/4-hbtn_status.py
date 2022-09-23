#!/usr/bin/python3
import requests
"""
Module: 4-htbn_status.py
"""

if __name__ == "__main__":
    r = requests.get("https://alx-intranet.hbtn.io/status")
    print(f"Body response:\n\t- type: {type(r.text)}",
          f"\n\t- content: {r.reason}")
