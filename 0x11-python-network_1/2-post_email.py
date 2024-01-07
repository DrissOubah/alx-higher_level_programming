#!/usr/bin/python3
"""
Sends a POST request to a given URL with a provided email.
Usage: ./post_email.py <URL> <email>
  - Displays the body of the response.
"""
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    target_url = sys.argv[1]
    email_value = {"email": sys.argv[2]}

    encoded_data = urllib.parse.urlencode(email_value).encode("ascii")

    post_request = urllib.request.Request(target_url, encoded_data)

    with urllib.request.urlopen(post_request) as response:
        print(response.read().decode("utf-8"))
