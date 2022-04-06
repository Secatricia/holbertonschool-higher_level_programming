#!/usr/bin/node

let secondBig = 0;
let firstBig = parseInt(process.argv[2]);
const argvlist = process.argv;
let j = 2;
let i = 2;

if (argvlist.length > 3) {
  for (j in argvlist) {
    if (parseInt(argvlist[j]) > firstBig) {
      firstBig = parseInt(argvlist[j]);
    }
    j++;
  }
  for (i in process.argv) {
    if (process.argv[i] > secondBig && process.argv[i] < firstBig) {
      secondBig = parseInt(process.argv[i]);
    }
    i++;
  }
}

console.log(secondBig);
