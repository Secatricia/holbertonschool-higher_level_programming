#!/usr/bin/node
/*
script that imports a dictionary of occurrences by user id and
computes a dictionary of user ids by occurrence
*/

const dict = require('./101-data.js').dict;
const newDict = {};

for (const [key, value] of Object.entries(dict)) {
  if (!new_dict[value]) { new_dict[value] = []; }
  new_dict[value].push(key);
}
console.log(new_dict);
