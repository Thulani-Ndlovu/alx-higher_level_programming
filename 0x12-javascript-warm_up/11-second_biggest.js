#!/usr/bin/node
const args = process.argv;
const array = [];
let sorted = [];
let count = 0;
if (!args[2] || args.length < 4) {
  console.log(0);
} else {
  for (let i = 2; i < args.length; i++) {
    array[count] = parseInt(args[i]);
    count++;
  }
  sorted = array.sort();
  console.log(sorted[sorted.length - 2]);
}
