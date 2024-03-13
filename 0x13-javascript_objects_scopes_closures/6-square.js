#!/usr/bin/node
const LastSquare = require('./5-square');

class Square extends LastSquare {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let charP = '';
      for (let j = 0; j < this.width; j++) {
        charP += c;
      }
      console.log(charP);
    }
  }
}

module.exports = Square;
