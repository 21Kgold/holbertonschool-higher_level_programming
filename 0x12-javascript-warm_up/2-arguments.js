#!/usr/bin/node
const message1 = 'No argument';
const message2 = 'Argument found';
const message3 = 'Arguments found';
const myVar = process.argv;
if (myVar.length < 3) {
  console.log(message1);
} else if (myVar.length === 3) {
  console.log(message2);
} else if (myVar.length >= 4) {
  console.log(message3);
}
