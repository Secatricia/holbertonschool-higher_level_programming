#!/usr/bin/node
/*
Write a script that imports an array and computes a new array.
*/
const list = require('./100-data').list;
const procesList = list.map((x, index) => x * index);
console.log(list);
console.log(procesList);