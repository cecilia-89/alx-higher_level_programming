#!/usr/bin/node
const request = require('request');

let count = 0;
const char = 'https://swapi-api.hbtn.io/api/people/18/';
request.get(process.argv[2], (error, response, body) => {
  if (!error) {
    const episodes = JSON.parse(body).results;
    episodes.forEach(episode => {
      if (episode.characters.includes(char)) {
        count++;
      }
    });
  }

  console.log(count);
});
