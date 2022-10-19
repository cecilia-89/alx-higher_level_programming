#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  }

  JSON.parse(body).characters.forEach(character => {
    request.get(character, (err, res, body) => {
      if (!err) {
        console.log(JSON.parse(body).name);
      }
    });
  });
});
