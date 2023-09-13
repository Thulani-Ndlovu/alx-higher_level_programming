#!/usr/bin/node
let newList = require('./100-data').list;
newList = newList.map((item, index) => (item * index));
console.log(newList);
