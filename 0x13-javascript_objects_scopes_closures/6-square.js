#!/usr/bin/node
const Rectangle = require('./4-rectangle.js');
module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (!c) {
      c = 'X';
    }
    let mysquare = '';
    for (let i = 0; i < this.width; i++) {
      mysquare += c;
    } for (let i = 0; i < this.height; i++) {
      console.log(mysquare);
    }
  }
};
