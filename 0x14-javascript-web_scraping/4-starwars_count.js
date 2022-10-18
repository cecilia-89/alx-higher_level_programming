#!/usr/bin/node
request = require('request')

let count = 0;
char = "https://swapi-api.hbtn.io/api/people/18/"
request.get(process.argv[2], (error, response, body) => {
	let episodes = JSON.parse(body)['results']
	episodes.forEach(episode => {
		if (episode['characters'].includes(char)){
			count++;
		}
	});

	console.log(count)
	}
)
