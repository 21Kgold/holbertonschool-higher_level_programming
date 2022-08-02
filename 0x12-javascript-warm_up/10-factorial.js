#!/usr/bin/node
function factorial (x) {
  if (x === 0 || x === 1) {
    return 1;
  } else {
    return x * factorial(x - 1);
  }
}
const x = parseInt(process.argv[2]);
if (!x) {
  console.log(1);
} else {
  console.log(factorial(x));
}
