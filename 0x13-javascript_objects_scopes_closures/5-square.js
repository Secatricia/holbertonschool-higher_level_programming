#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
	for (let i = 0; i < this.height; i++) {
		for (let i = 0; i < this.width; i++) {
		  process.stdout.write('X');
		}
		console.log('');
	  }
  }

  rotate () {
    const cpheight = this.height;
    this.height = this.width;
    this.width = cpheight;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}

module.exports = Rectangle;
module.exports = Square;
