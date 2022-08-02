#!/usr/bin/node
const message2 = 'Missing size';
if (!process.argv[2]) {
  console.log(message2);
} else if (parseInt(process.argv[2]) && process.argv[2] > 0) {
  for (let i = 0; i < parseInt(process.argv[2]); i++) {
    let square = '';
    for (let i = 0; i < parseInt(process.argv[2]); i++) {
      square += 'X';
    }
    console.log(square);
  }
}
