#!/usr/bin/node
const request = require('request');

let count = 0;
request.get(process.argv[2], (error, response, body) => {
  if (!error) {
    const episodes = JSON.parse(body).results;
    episodes.forEach(episode => {
      episode.characters.forEach(char => {
        if (char.endsWith('/18/')) {
          count++;
        }
      });
    });
  }

  console.log(count);
});
