#!/usr/bin/node
const axios = require('axios').default;
const fs = require('fs');
const uri = process.argv[2];
const path = process.argv[3];
axios.get(uri)
  .then((response) => {
    fs.writeFile(path, response.data, 'utf-8', (err, result) => {
      if (err) {
        console.log(err);
      }
    });
  })
  .catch((error) => {
    if (error.response) {
      console.log('code: ' + error.response.status);
    }
  });
