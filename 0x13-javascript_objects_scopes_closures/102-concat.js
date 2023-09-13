#!/usr/bin/node
const fs = require('fs');
const args = process.argv;

const fileA = args[1];
const fileB = args[2];
const fileC = args[3];

function concatenateFiles (source1, source2, destination) {
  if (args.length < 4) {
    return -1;
  }
  const data1 = fs.readFileSync(source1, 'utf8');
  const data2 = fs.readFileSync(source2, 'utf8');
  const concatenatedData = data1 + '\n' + data2;
  fs.writeFileSync(destination, concatenatedData);
}
concatenateFiles(fileA, fileB, fileC);
