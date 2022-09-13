#!/usr/bin/node
// Script that display the status code of a HTTP Get request

const axios = require('axios');
axios.get(process.argv[2])
  .then((res) => {
    console.log(`code: ${res.status}`);
  }).catch(function (error) {
    if (error.response) {
      console.log('code:', error.response.status);
    }
  });
