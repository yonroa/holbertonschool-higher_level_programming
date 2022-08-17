#!/usr/bin/node
const file = process.argv[2];
const fs = require('fs');
fs.readFile(file, 'utf-8', (err, result) => {
  if (err) {
    console.log(err);
  } else {
    console.log(result);
  }
});
