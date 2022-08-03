#!/usr/bin/node
if (!process.argv[3]) {
  console.log(0);
} else {
  let i = 2;
  let j = 0;
  let k = 2;
  let l = 0;
  for (i = 2; i < process.argv.length; i++) {
    if (parseInt(process.argv[i]) > j) {
      j = parseInt(process.argv[i]);
    }
  } for (k = 2; k < process.argv.length; k++) {
    if (parseInt(process.argv[k]) < j && parseInt(process.argv[k]) > l) {
      l = parseInt(process.argv[k]);
    }
  }
  console.log(l);
}
