#!/usr/bin/node
// Script that prints the number of movies where the character
// “Wedge Antilles” is present, using the (Wedge Antilles is character ID 18)
// Star Wars API available at the endpoint
// https://swapi-api.hbtn.io/api/films/ using the module axios

const axios = require('axios');
const args = process.argv;
axios.get(args[2])
  .then(function (response) {
    const films = response.data.results;
    let match = 0;
    for (let i = 0; i < films.length; i++) {
      const characters = films[i].characters;
      for (let j = 0; j < characters.length; j++) {
        if (characters[j] === 'https://swapi-api.hbtn.io/api/people/18/') {
          match++;
        }
      }
    }
    console.log(match);
  });
