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
    if (movie.characters.includes('https://swapi-api.hbtn.io/api/people/18/')) {
      amount++;
    }
  }
  console.log(amount);
});
