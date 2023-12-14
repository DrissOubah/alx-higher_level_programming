#!/usr/bin/node
const listData = require('./100-data.js');
const list = listData.list;
console.log(list);
const map1 = list.map((value,index) => value * index);

console.log(map1);
