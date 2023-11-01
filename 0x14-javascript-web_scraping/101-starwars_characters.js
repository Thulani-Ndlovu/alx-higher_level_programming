#!/usr/bin/node

const request = require('request');

function getData (url) {
  return new Promise((resolve, reject) => {
    request(url, (e, res, body) => {
      if (e) {
        reject(e);
      } else {
        resolve(body);
      }
    });
  });
}

function errorHandler (e) {
  console.log(e);
}

function movieCharacters (movieId) {
  const movieAPI = `https://swapi-api.alx-tools.com/api/films/${movieId}`;
  getData(movieAPI).then(JSON.parse, errorHandler).then((res) => {
    const chars = res.characters;
    const promises = {};

    for (let i = 0; i < chars.length; ++i) {
      promises.push(getData(chars[i]));
    }

    Promise.all(promises).then((result) => {
      for (let j = 0; j < result.length; ++j) {
        console.log(JSON.parse(result[j]).name);
      }
    }).catch((error) => {
      console.log(error);
    });
  });
}

movieCharacters(process.argv[2]);
