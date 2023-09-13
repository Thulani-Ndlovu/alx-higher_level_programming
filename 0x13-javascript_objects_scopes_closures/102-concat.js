#!/usr/bin/node
const fs = require('fs');
const args = process.argv;
const fileA = fs.readFileSync(args[2]).toString();
const fileB = fs.readFileSync(args[3]).toString();
fs.writeFileSync(args[4], fileA + fileB);