#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  }

  const jsonResponse = JSON.parse(body);

  let amount = 0;
  for (const result of jsonResponse.results) {
    for (const character of result.characters) {
      if (character === 'https://swapi-api.hbtn.io/api/people/18/') {
        amount += 1;
      }
    }
  }
  console.log(amount);
});
