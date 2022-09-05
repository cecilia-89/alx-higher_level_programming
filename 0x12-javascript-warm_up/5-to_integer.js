#!/usr/bin/node
const parsed = Number(process.argv[2], 2);
if (isNaN(parsed)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parsed);
}
