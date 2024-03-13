#!/usr/bin/node
exports.addMeMaybe = function (number, theFunction) {
  const nb = theFunction(number + 1);
  return nb;
};
