#!/usr/bin/python3
"""
script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    target_url = sys.argv[1]
    email_param = {"email": sys.argv[2]}
    encoded_data = urllib.parse.urlencode(email_param).encode("ascii")

    post_request = urllib.request.Request(target_url, encoded_data)
    with urllib.request.urlopen(post_request) as response:
        print(response.read().decode("utf-8"))
