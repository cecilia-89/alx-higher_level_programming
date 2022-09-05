#!/usr/bin/node
function fac (num) {
  if (isNaN(num) || num === 1) {
    return 1;
  }

  return fac(num - 1) * num;
}

console.log(fac(process.argv[2]));
