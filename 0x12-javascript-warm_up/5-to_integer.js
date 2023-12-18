#!/usr/bin/node
const { argv } = require('process');
const integerValue = parseInt(argv[2]);
if (!isNaN(integerValue)) {
  console.log('My number:', integerValue);
} else {
  console.log('Not a number');
}
