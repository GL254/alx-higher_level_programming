#!/usr/bin/node
/*
 * creates a Square class that inherits from Rectangle
 */
const Square = require('./5-square');
class square extends Square {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let printed = 'X';
    if (c === undefined) {
      printed = 'X';
    } else { printed = c; }
    for (let i = 0; i < this.size; i++) { console.log(printed.repeat(this.size)); }
  }
}
module.exports = square;
