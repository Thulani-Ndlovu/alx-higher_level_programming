const dictionary = require('./101-data').dict;
const userIdsByOccurrence = {};

for (const userId in dictionary) {
  const occurrence = dictionary[userId];

  if (!(occurrence in userIdsByOccurrence)) {
    userIdsByOccurrence[occurrence] = [];
  }
  userIdsByOccurrence[occurrence].push(userId);
}
console.log(userIdsByOccurrence);
