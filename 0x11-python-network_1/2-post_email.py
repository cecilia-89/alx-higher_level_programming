#!/usr/bin/python3
""" Module: 2-post_email.py """

from urllib import request, parse
from sys import argv

if __name__ == "__main__":
    param = {'email': argv[2]}
    query_string = parse.urlencode(param)
    url = f"{argv[1]}?{query_string}
    with request.urlopen(url) as resp:
        data = resp.read()
        print(data.decode('utf-8'))
