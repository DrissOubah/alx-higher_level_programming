#!/usr/bin/node
const dict = require('./101-data.js').dict;

const newDict = {};

Object.keys(dict).forEach(userId => {
  const occurrences = dict[userId];
  newDict[occurrences] = newDict[occurrences] || [];
  newDict[occurrences].push(userId);
});

console.log(newDict);
