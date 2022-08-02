#!/usr/bin/node
const message1 = ' is ';
const message2 = 'undefined';
if (process.argv[2] && process.argv[3]) {
  console.log(process.argv[2] + message1 + process.argv[3]);
} else if (process.argv[2]) {
  console.log(process.argv[2] + message1 + message2);
} else if (!process.argv[2]) {
  console.log(message2 + message1 + message2);
}
