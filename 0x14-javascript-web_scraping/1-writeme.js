#!/usr/bin/node
// Script that writes a string to a file

const fs = require('fs');
fs.writeFile(process.argv[2], process.argv[3], (err, data) => {
  if (err) {
    console.error(err);
  }
});
