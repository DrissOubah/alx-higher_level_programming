#!/usr/bin/node
const { argv } = require('process');
function fact (x) {
  if (x === 0 || x === 1 || isNaN(x)) {
    return 1;
  } else {
    return x * fact(x - 1);
  }
}
console.log(fact(parseInt(argv[2])));
