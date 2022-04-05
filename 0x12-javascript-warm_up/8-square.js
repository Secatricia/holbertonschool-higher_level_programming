#!/usr/bin/node

const a = process.argv[2];

if (parseInt(process.argv[2]) && process.argv[2] > 0) {
  while (process.argv[2] !== 0) {
    console.log('X'.repeat(a));
    process.argv[2] -= 1;
  }
} else {
  console.log('Missing size');
}
