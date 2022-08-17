#!/usr/bin/node
const axios = require('axios').default;
axios.get('https://swapi-api.hbtn.io/api/films/' + process.argv[2])
  .then((response) => {
    const title = 'title';
    console.log(response.data[title]);
  })
  .catch((error) => {
    if (error.response) {
      console.log('code: ' + error.response.status);
    }
  });
