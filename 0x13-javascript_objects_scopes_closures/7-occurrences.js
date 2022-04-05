#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let counter = 0;
  let i = 0;
  for (i in list) {
    if (list[i] === searchElement) {
      counter += 1;
    }
  }
  return (counter);
};
