#!/usr/bin/python3
"""
Displays the X-Request-Id header variable of a request to a given URL.
Usage: ./get_request_id.py <URL>
"""
import sys
import requests


if __name__ == "__main__":
    target_url = sys.argv[1]
    response = requests.get(target_url)
    request_id = response.headers.get("X-Request-Id")
    print(request_id)
