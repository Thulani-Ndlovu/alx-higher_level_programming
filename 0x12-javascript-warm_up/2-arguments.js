#!/usr/bin/node
const args = process.argv;
if (args.length <= 0) {
  console.log('No argument');
}
if (args.length === 1) {
  console.log('Argument found');
}
if (args.length > 1) {
  console.log('Arguments found');
}
