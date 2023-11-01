#!/usr/bin/node

const request = require('request');

request(process.argv[2], (e, res, body) => {
  if (e) {
    console.log(e);
  } else {
    const tasksCompletedByUserId = {};
    body = JSON.parse(body);

    for (let i = 0; i < body.length; ++i) {
      const userId = body[i].userId;
      const completed = body[i].completed;

      if (completed && !tasksCompletedByUserId[userId]) {
        tasksCompletedByUserId[userId] = 0;
      }
      if (completed) ++tasksCompletedByUserId[userId];
    }

    console.log(tasksCompletedByUserId);
  }
});
