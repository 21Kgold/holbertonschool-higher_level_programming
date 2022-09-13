#!/usr/bin/node
// Script that display the status code of a GET request

const axios = require('axios');
axios.get(process.argv[2])
  .then((res) => {
    console.log(`Code: ${res.status}`);
  }).catch(function (error) {
    if (error.response) {
      console.log('Code:', error.response.status);
    }
  });
