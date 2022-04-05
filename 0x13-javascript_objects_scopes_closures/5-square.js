#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
      this.cpwidth = w;
      this.cpheight = h;
    }
  }

  print () {
    while (this.height !== 0) {
      console.log('X'.repeat(this.width));
      this.height -= 1;
    }
    this.width = this.cpwidth;
    this.height = this.cpheight;
  }

  rotate () {
    this.width = this.cpheight;
    this.height = this.cpwidth;
    this.cpheight = this.width;
    this.cpwidth = this.height;
  }

  double () {
    this.width = this.cpwidth * 2;
    this.height = this.cpheight * 2;
    this.cpwidth = this.width;
    this.cpheight = this.height;
  }
}

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}

module.exports = Rectangle;
module.exports = Square;
