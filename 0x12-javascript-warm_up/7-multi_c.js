#!/usr/bin/node
if (parseInt(process.argv[2])) {
  while (process.argv[2] > 0) {
    console.log('C is fun');
    process.argv[2] -= 1;
  }
} else {
  console.log('Missing number of occurrences');
}
