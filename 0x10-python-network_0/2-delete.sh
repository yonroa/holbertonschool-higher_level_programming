#!/bin/bash
# takes in a URL and displays all HTTP methods the server will accept
curl -sL "$1" -X DELETE
