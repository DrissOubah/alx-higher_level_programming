#!/usr/bin/python3
"""
Script that fetches a URL with the requests package.
"""
import requests


if __name__ == "__main__":
    response = requests.get('https://alx-intranet.hbtn.io/status')
    response_text = response.text

    print('Body response:\n\t- type: {}\n\t- content: {}'.format(
            type(response_text), response_text))
