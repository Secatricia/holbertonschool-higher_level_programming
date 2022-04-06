#!/usr/bin/node

let secondBig = 0;
let firstBig = 0;

if (process.argv[2] === undefined || process.argv[3] === undefined) {
  console.log('0');
} else {
  for (let j in process.argv) {
    if (process.argv[j] > firstBig) {
      firstBig = process.argv[j];
    }
    j++;
  }
  for (let i in process.argv) {
    if (process.argv[i] > secondBig) {
      if (process.argv[i] < firstBig) {
        secondBig = process.argv[i];
      } else {
        firstBig = process.argv[i];
      }
    }
    i++;
  }
  console.log(secondBig);
}
