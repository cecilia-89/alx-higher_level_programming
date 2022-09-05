#!/usr/bin/node
let res = 0;
const args = process.argv.slice(2);
console.log(args)
if (args.length > 1) {
  args.sort();
  console.log(args)
}
console.log(res);
