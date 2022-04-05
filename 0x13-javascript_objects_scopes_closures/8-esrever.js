#!/usr/bin/node

exports.esrever = function (list) {
  let lengthl = list.length;
  let i = 0;
  let cpList;

  while (i < list.length / 2) {
    cpList = list[i];
    list[i] = list[lengthl - 1];
    list[lengthl - 1] = cpList;
    i++;
    lengthl -= 1;
  }
  return (list);
};
