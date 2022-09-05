#!/usr/bin/node
const parsed = Number(process.argv[2], 2);
if (isNaN(parsed)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < process.argv[2]; i++) {
    console.log('X'.repeat(process.argv[2]));
  }
}
