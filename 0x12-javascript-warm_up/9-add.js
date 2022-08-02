#!/usr/bin/node
const message2 = 'NaN';
if (!parseInt(process.argv[2]) || !parseInt(process.argv[3])) {
  console.log(message2);
} else {
  console.log(parseInt(process.argv[2]) + parseInt(process.argv[3]));
}
