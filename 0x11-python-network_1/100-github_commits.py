#!/usr/bin/python3
"""list 10 commits (from the most recent to oldest) of an repository
"""
if __name__ == "__main__":
    import requests
    import sys
    r = requests.get(
        'https://api.github.com/repos/{}/{}/commits'.format(sys.argv[2], sys.argv[1]))
    commits = r.json()
    for commit in commits[:10]:
        print(commit.get('sha'), end=': ')
        print(commit.get('commit').get('author').get('name'))
