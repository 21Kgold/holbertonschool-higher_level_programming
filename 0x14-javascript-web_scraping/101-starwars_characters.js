#!/usr/bin/node
// Script that prints all characters of a Star Wars movie:
// The first argument is the Movie ID - example: 3 = “Return of the Jedi”
// Display one character name by line
// Use the starwars Api https://swapi-api.hbtn.io/

const axios = require('axios');
const episode = process.argv[2];
if (episode < 1 || isNaN(episode) === true) {
	return;
} else {
const URL = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
axios.get(URL)
  .then(function (response) {
    const films = response.data.characters;
    for (let i = 0; i < films.length; i++) {
      axios.get(films[i])
        .then(function (res) {
          const name = res.data.name;
          console.log(name);
        });
    }
  });
}
