#!/usr/bin/node

const request = require('request');
const url = process.argv[1];

request(url, function (error, response, body) {
    console.log('code: ', response && response.statusCode);
});
