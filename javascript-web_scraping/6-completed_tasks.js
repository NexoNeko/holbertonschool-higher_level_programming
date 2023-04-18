#!/usr/bin/node

const request = require('request');
const _everyone = process.argv[2];

request(_everyone, function (error, response, body) {
  if (error) {
    console.log('error:', error);
  }

  const everyTodo = JSON.parse(body);
  const completed = {};

  everyTodo.forEach((task) => {
    if (task.completed && completed[task.userId] === undefined) {
      completed[task.userId] = 1;
    } else if (task.completed) {
      completed[task.userId] += 1;
    }
  });

  console.log(completed);
});
