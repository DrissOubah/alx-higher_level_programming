#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL
and displays the body of the response.
Usage: ./check_http_status.py <URL>
  - Handles HTTP errors.
"""
import sys
import requests


if __name__ == "__main__":
    target_url = sys.argv[1]
    response = requests.get(target_url)

    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)
