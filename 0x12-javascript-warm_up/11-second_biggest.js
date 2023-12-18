#!/usr/bin/node
const { argv } = require('process');
if (argv.length <= 3) {
  console.log('0');
} else {
  const args = process.argv.slice(2).map(Number);
  const sortedArgs = args.sort((a, b) => parseInt(b) - parseInt(a));
  console.log(sortedArgs[1]);
}
