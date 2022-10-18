#!/usr/bin/node
const request = require('request');

let count = 0;
request.get(process.argv[2], (error, response, body) => {
  if (!error) {
    const episodes = JSON.parse(body).results;
    episodes.forEach(episode => {
      console.log(episode.charcters)
    });
  }

  console.log(count);
});
