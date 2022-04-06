#!/usr/bin/node

let secondBig = 0;
let firstBig = 0;
const argvlist = process.argv;

if (argvlist.length > 3) {
  for (let j in argvlist) {
    if (argvlist[j] > firstBig) {
      firstBig = argvlist[j];
    }
    j++;
  }

  for (let i in process.argv) {
    if (process.argv[i] > secondBig && process.argv[i] < firstBig) {
      secondBig = process.argv[i];
    }
    i++;
  }
}

console.log(secondBig);
