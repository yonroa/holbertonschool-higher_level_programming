#!/usr/bin/python3
"""takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter
"""
if __name__ == "__main__":
    import requests
    import sys
    payload = {'q': ""}
    if len(sys.argv) == 2:
        payload = {'q': sys.argv[1]}
    r = requests.post('http://0.0.0.0:5000/search_user', data=payload)
    try:
        r_dict = r.json()
        r_id = r_dict.get('id')
        r_name = r_dict.get('name')
        if len(r_dict) == 0 or not r_id or not r_name:
            print("No result")
        else:
            print("[{}] {}".format(r_id, r_name))
    except:
        print('Not a valid JSON')
