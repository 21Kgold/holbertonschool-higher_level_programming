#!/usr/bin/node
const message1 = 'C is fun';
const message2 = 'Missing number of occurrences';
if (!process.argv[2]) {
  console.log(message2);
} else if (parseInt(process.argv[2]) && process.argv[2] > 0) {
  for (let i = 0; i < parseInt(process.argv[2]); i++) {
    console.log(message1);
  }
}
