#!/usr/bin/node

const fs = require('fs');

fs.readFile(process.arg[2], 'utf8', function (e, info_) {
  if (e) {
    console.log(e);
  } else {
    process.stdout.write(info_);
  }
});
