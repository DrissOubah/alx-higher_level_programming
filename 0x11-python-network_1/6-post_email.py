#!/usr/bin/python3
"""
Sends a POST request to a given URL with a provided email.
Usage: ./post_email_requests.py <URL> <email>
  - Displays the body of the response.
"""
import sys
import requests


if __name__ == "__main__":
    target_url = sys.argv[1]
    email_value = {"email": sys.argv[2]}
    response = requests.post(target_url, data=email_value)
    print(response.text)
