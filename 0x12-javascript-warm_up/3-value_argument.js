#!/usr/bin/node
const message1 = 'No argument';
if (process.argv[2]) {
  console.log(process.argv[2]);
} else {
  console.log(message1);
}
