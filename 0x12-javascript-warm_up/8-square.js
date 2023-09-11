#!/usr/bin/node
const args = process.argv;
let square = '';
if (!args[2] || !parseInt(args[2])) {
  console.log('Missing size');
} else if (args[2] > 0) {
  const squareSize = parseInt(args[2]);
  for (let i = 0; i < squareSize; i++) {
    for (let j = 0; j < squareSize; j++) {
      square += 'X';
    }
    if (i < squareSize - 1) {
      square += '\n';
    }
  }
  console.log(square);
}
