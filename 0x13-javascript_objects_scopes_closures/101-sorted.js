#!/usr/bin/node
const dict = require('./101-data').dict;
const myDict = {};
for (const ocurrence in dict) {
  if (!myDict[dict[ocurrence]]) {
    myDict[dict[ocurrence]] = [];
  }
  myDict[dict[ocurrence]].push(ocurrence);
}
console.log(myDict);
