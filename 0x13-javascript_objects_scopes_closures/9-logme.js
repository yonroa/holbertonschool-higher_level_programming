#!/usr/bin/node
let nPrint = 0;
exports.logMe = function (item) {
  console.log(nPrint + ': ' + item);
  nPrint++;
};
