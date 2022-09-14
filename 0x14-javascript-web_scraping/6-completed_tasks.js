#!/usr/bin/node
// Script that computes the number of tasks completed by user id.
// The first argument is the API URL https://jsonplaceholder.typicode.com/todos
// Only print users with completed task

const axios = require('axios');
axios.get(process.argv[2])
  .then(function (response) {
    const tasks = response.data;
    const doneTasks = {};
    for (let i = 0; i < tasks.length; i++) {
      if (tasks[i].completed === true) {
        if (tasks[i].userId in doneTasks === false) {
          doneTasks[tasks[i].userId] = 1;
        } else {
          doneTasks[tasks[i].userId] = doneTasks[tasks[i].userId] + 1;
        }
      }
    }
    console.log(doneTasks);
  });
