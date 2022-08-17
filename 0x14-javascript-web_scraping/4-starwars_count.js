#!/usr/bin/node
const axios = require('axios').default;
const results = 'results';
const characters = 'characters';
axios.get(process.argv[2])
  .then((response) => {
    let count = 0;
    for (let j = 0; j < response.data[results].length; j++) {
      count += search18(response.data[results][j][characters]);
    }
    console.log(count);
  })
  .catch((error) => {
    if (error.response) {
      console.log('code: ' + error.response.status);
    }
  });

function search18 (data) {
  const Wedge = 'https://swapi-api.hbtn.io/api/people/18/';
  for (let i = 0; i < data.length; i++) {
    if (data[i] === Wedge) {
      return 1;
    }
  }
  return 0;
}
