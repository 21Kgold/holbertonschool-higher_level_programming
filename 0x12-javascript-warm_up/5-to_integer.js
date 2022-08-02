#!/usr/bin/node
const message1 = 'Not a number';
const message2 = 'My number: ';
if (!process.argv[2]) {
  console.log(message1);
} else if (parseInt(process.argv[2])) {
  console.log(message2 + parseInt(process.argv[2]));
} else {
  console.log(message1);
}
