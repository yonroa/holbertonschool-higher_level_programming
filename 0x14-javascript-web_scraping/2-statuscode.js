#!/usr/bin/node
const axios = require('axios').default;
axios.get(process.argv[2])
  .then((response) => {
    console.log('code: ' + response.status);
  })
  .catch((error) => {
    if (error.response) {
      console.log('code: ' + error.response.status);
    }
  });
