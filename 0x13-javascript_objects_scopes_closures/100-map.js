#!/usr/bin/node
let newList = require('./100-data').list;
console.log(newList);
newList = newList.map((item, index) => (item * index));
console.log(newList);
