#!/usr/bin/node
request = require('request')
const fs = require('fs');

request.get(process.argv[2]).pipe(fs.createWriteStream('loripsum'))