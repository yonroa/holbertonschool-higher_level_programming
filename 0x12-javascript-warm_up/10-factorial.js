#!/usr/bin/node
function factorial (num) {
  if (num === 1 || num == null) {
    return 1;
  }
  return (num * factorial(num - 1));
}
console.log(factorial(process.argv[2]));
