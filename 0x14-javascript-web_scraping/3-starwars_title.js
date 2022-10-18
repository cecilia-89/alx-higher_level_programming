#!/usr/bin/node
request = require('request')

url = "https://swapi-api.hbtn.io/api/films/"
request.get(url + process.argv[2], (error, response, body) => {
	console.log(JSON.parse(body)['title'])
})