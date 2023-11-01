#!/usr/bin/node

const request = require('request');
const starWarsAPI = process.argv[2];
let count = 0;

request(starWarsAPI, (e, res, body) => {
  body = JSON.parse(body).results;

  for (let i = 0; i < body.length; ++i) {
    const chars = body[i].characters;

    for (let j = 0; j < chars.length; ++j) {
      const char = chars[j];
      const charId = char.split('/')[5];

      if (charId === '18') {
        count += 1;
      }
    }
  }
  console.log(count);
});
