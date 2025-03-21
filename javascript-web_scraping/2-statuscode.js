#!/usr/bin/node

const url = process.argv[1];

fetch(url).then(res => {
  console.log('code:' + res.status);
});
