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
  for (let i = 0; i < data.length; i++) {
    const character = data[i];
    const characterId = character.split('/')[5];
    if (characterId === '18') {
      return 1;
    }
  }
  return 0;
}
