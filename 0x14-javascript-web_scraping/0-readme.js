#!/usr/bin/node
// Script that reads and prints the content of a file

/* Get file system module */
const fs = require('fs');
/* Get all the content of a file */
fs.readFile(process.argv[2], 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data.toString());
});
