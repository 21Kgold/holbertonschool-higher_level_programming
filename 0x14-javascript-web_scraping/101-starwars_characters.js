#!/usr/bin/node
// Script that prints all characters of a Star Wars movie:
// The first argument is the Movie ID - example: 3 = “Return of the Jedi”
// Display one character name by line, same order as the object
// Use the starwars Api https://swapi-api.hbtn.io/


const request = require('request');
const episode = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + episode;

function checkCharacter (characters, numChar) {
  if (numChar === characters.length) {
    return;
  }
  request(characters[numChar], function (error2, response2, body2) {
    if (error2) {
      console.log('code:', response2.statusCode);
    }
    console.log(JSON.parse(body2).name);
    checkCharacter(characters, numChar + 1);
  });
}

request(url, function (error, response, body) {
  if (error) {
    console.log('code:', response.statusCode);
  } else {
    const jsonBody = JSON.parse(body);
    checkCharacter(jsonBody.characters, 0);
  }
});
