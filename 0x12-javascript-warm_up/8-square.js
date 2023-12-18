#!/usr/bin/node
const { argv } = require('process');
if (isNaN(parseInt(argv[2]))) {
  console.log('Missing size');
} else {
  for (let i = 0; i < argv[2]; i++) {
    let x = '';
    for (let j = 0; j < argv[2]; j++) {
      x += 'X';
    }
    console.log(x);
  }
}
