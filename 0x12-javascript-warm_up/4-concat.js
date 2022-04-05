#!/usr/bin/node

if (process.argv[2] === undefined) {
<<<<<<< HEAD
  console.log('undefined is undefined');
}
if (process.argv[2] !== undefined && process.argv[3] === undefined) {
  console.log(process.argv[2] + ' is undefined');
}
if (process.argv[3] !== undefined) {
  console.log(process.argv[2] + ' is ' + process.argv[3]);
=======
	console.log('undefined is undefined');
}
if (process.argv[2] !== undefined && process.argv[3] === undefined) {
	console.log(process.argv[2] + ' is undefined');
}
if (process.argv[3] !== undefined) {
	console.log(process.argv[2] + ' is ' + process.argv[3]);
>>>>>>> adfd7f7321f0676258dfbf66ca145696431d6d42
}
