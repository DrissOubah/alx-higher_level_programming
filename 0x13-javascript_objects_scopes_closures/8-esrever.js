#!/usr/bin/node
exports.esrever = function (list) {
  let len = list.length - 1;
  let i = 0;
  while ((len - i) > 0) {
    const nel = list[len];
    list[len] = list[i];
    list[i] = nel;
    i++;
    len--;
  }
  return list;
};
