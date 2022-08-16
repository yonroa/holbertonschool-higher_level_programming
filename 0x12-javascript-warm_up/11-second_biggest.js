#!/usr/bin/node
if (process.argv.lenght < 3) {
  console.log(0);
} else {
  const array = process.argv.slice(2).map(Number);
  console.log(array.sort((a, b) => b - a)[1]);
}
