#!/usr/bin/python3
"""script that fetches https://intranet.hbtn.io/status"""
if __name__ == "__main__":
    import requests
    r = requests.get('https://intranet.hbtn.io/status').text
    print('Body response:')
    print(f"\t- type: {type(r)}")
    print(f"\t- content: {r}")
