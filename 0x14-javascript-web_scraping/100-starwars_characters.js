#!/usr/bin/node

const request = require('request');
const starWarsAPI = 'https://swapi-api.alx-tools.com/api/films/'.concat(process.argv[2]);

request(starWarsAPI, (e, res, body) => {
  const chars = JSON.parse(body).characters;

  for (let i = 0; i < chars.length; ++i) {
    request(chars[i], (e2, res2, body2) => {
      console.log(JSON.parse(body2).name);
    });
  }
});
