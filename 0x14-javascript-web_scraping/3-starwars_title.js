#!/usr/bin/node
// Script that retrieves the Film name that match an integerer using the The
// Star Wars API available at the endpoint
// https://swapi-api.hbtn.io/api/films/:id using the module axios

const axios = require('axios');
const URL = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
axios.get(URL)
  .then(function (response) {
    console.log(response.data.title);
  });
