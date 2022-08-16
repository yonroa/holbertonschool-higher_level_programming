#!/usr/bin/node
const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c = 'X') {
    const char = c;
    for (let i = 0; i < this.width; i++) {
      console.log(char.repeat(this.width));
    }
  }
}
module.exports = Square;
