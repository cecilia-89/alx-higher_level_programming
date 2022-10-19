#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  const ep = JSON.parse(body);
  displayChar(ep.characters, 0);
});

function displayChar (chars, count) {
  request.get(chars[count], (err, res, body) => {
    if (!err) {
      console.log(JSON.parse(body).name);

      if (count++ < chars.length) {
        displayChar(chars, count);
      }
    }
  });
}
