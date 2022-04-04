#!/usr/bin/node

if (process.argv[2] === undefined) {
	console.log('undefined is undefined');
}
if (process.argv[2] !== undefined && process.argv[3] === undefined) {
	console.log(process.argv[2] + ' is undefined');
}
if (process.argv[3] !== undefined) {
	console.log(process.argv[2] + ' is ' + process.argv[3]);
}
