#!/usr/bin/python3
"""takes in a URL and an email, sends a POST request to the passed
URL with the email as a parameter, and displays the body of the response
"""
if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys
    value = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(value).encode('utf-8')
    req = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8', 'replace'))
