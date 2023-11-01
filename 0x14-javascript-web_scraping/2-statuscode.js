#!/usr/bin/node

const request = require('request');

request(process.argv[2], (e, res) => {
  console.log('code:', res.statusCode);
});
