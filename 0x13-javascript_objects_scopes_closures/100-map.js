#!/usr/bin/node
const list = require('./100-data').list;
let map1 = [];
let i = 0;
map1 = list.map(x => x * i++);
console.log(list);
console.log(map1);
