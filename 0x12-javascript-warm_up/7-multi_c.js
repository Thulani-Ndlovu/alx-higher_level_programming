#!/usr/bin/node
const args = process.argv;
if (!args[2]) {
  console.log('Missing number of occurrences');
}
if (args[2] > 0) {
  const times = parseInt(args[2]);
  for (let i = 0; i < times; i++) {
    console.log('C is fun');
  }
}
