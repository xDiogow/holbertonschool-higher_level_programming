#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  }

  const jsonResponse = JSON.parse(body);

  let amount = 0;
  for (const movie of jsonResponse.results) {
    for (const character of movie.characters) {
      if (character.endsWith('/18/')) {
        amount++;
        break;
      }
    }
  }
  console.log(amount);
});
