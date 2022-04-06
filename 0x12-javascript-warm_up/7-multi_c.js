#!/usr/bin/node
if (Number(process.argv[2]) && process.argv[2] > 0) {
  while (process.argv[2] > 0) {
    console.log('C is fun');
    process.argv[2] -= 1;
  }
} else {
  console.log('Missing number of occurrences');
}
