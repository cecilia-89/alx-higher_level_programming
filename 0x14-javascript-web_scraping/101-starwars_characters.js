#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  }


  for (const i in JSON.parse(body).characters) {
    request.get(JSON.parse(body).characters[i], (err, res, body) => {
      if (!err) {
        console.log(JSON.parse(body).name);
      }
    });
  }

});
