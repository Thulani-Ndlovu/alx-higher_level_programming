#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    if (!this.width && !this.height) {
      return;
    }
    let screen = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        screen += 'X';
      }
      if (i < this.height - 1) {
        screen += '\n';
      }
    }
    console.log(screen);
  }
}
module.exports = Rectangle;
