#!/usr/bin/node

const request = require('request');
const starWarsAPI = 'https://swapi-api.alx-tools.com/api/films/'.concat(process.argv[2]);

request(starWarsAPI, (e, res, body) => {
  body = JSON.parse(body);
  console.log(body.title);
});
