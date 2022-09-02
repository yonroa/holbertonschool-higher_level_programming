#!/usr/bin/python3
"""takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""
if __name__ == "__main__":
    import requests
    import sys
    params = {'Authorization': 'token ' + sys.argv[2]}
    r = requests.get(
        "https://api.github.com/users/{}".format(sys.argv[1]), headers=params)
    print(r.json().get('id'))
