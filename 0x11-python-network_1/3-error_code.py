#!/usr/bin/python3
"""
Sends a request to a given URL and displays the response body.
Usage: ./check_http_status.py <URL>
  - Handles HTTP errors.
"""
import sys
import urllib.error
import urllib.request


if __name__ == "__main__":
    target_url = sys.argv[1]

    http_request = urllib.request.Request(target_url)
    try:
        with urllib.request.urlopen(http_request) as response:
            print(response.read().decode("ascii"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
