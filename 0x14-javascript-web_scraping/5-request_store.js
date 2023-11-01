#!/usr/bin/node

const request = require('request');
const fs = require('fs');

request(process.argv[2], (e, res, body) => {
  fs.writeFile(process.argv[3], body, 'utf8', (e2) => {
    if (e2) {
      console.log(e2);
    }
  });
});
