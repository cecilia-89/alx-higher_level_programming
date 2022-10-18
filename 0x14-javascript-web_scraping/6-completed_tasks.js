#!/usr/bin/node
const request = require('request')

request.get(process.argv[2], (error, response, body) => {
	const completed = {}
	JSON.parse(body).forEach(user => {
		if (user.completed && completed[user.userId] === undefined){
			completed[user.userId] = 1
		} else if (user.completed){
			completed[user.userId] += 1
		}
	})
	console.log(completed)
})