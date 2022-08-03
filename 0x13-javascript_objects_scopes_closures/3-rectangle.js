#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
    this.print = function () {
      let square = '';
      for (let i = 0; i < w; i++) {
        square += 'X';
      } for (let i = 0; i < h; i++) {
        console.log(square);
      }
    };
  }
};
