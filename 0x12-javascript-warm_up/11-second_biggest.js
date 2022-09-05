#!/usr/bin/node
let res = 0;
const args = process.argv.slice(2);

if (args.length > 1) {
  res = args.sort(function (a, b) { return b - a; })[1];
}
console.log(res);
