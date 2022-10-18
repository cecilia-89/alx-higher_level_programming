#!/usr/bin/node
request = require('request')

request.get(process.argv[2], (error, response, body) => {
	let json_obj = {}
	JSON.parse(body).forEach(user => {

		if (user.json_obj && json_obj[user.userId] === undefined){
			json_obj[id] = 0
		} else if (user.completed){
			user.completed += 1
		}

	})
	console.log(json_obj)
})