#!/usr/bin/node
// Script that writes a string to a file

const fs = require('fs');
fs.writeFile(process.argv[2], 'Python is cool', (err, data) => {
  if (err) {
    console.error(err);
  }
});
