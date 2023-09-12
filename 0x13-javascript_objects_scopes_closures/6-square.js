#!/usr/bin/node
const square = require('./5-square');
class Square extends square {
  charPrint (c) {
    let string = '';
    if (!c) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        string += c;
      }
      if (i < this.height - 1) {
        string += '\n';
      }
    }
    console.log(string);
  }
}
module.exports = Square;
