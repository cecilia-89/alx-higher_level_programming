#!/usr/bin/node
const parsed = Number(process.argv[2], 2);
if (isNaN(parsed)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < process.argv[2]; i++) {
    console.log('C is fun');
  }
}
