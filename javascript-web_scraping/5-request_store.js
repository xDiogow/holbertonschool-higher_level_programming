const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const fileName = process.argv[3];

request(url, 'utf-8', function (error, response, body) {
  if (error) {
    console.log(error);
  }

  fs.writeFile(fileName, body, function (err) {
    if (err) {
      console.log(err);
    }
  });
});
