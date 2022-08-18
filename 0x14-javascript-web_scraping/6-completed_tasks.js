#!/usr/bin/node
const axios = require('axios').default;
axios.get(process.argv[2])
  .then((response) => {
    const completeTasks = {};
    for (let i = 0; i < response.data.length; i++) {
      const userId = response.data[i].userId;
      const completed = response.data[i].completed;
      if (completed && !completeTasks[userId]) {
        completeTasks[userId] = 0;
      }
      if (completed) ++completeTasks[userId];
    }
    console.log(completeTasks);
  })
  .catch((error) => {
    if (error.response) {
      console.log('code: ' + error.response.status);
    }
  });
