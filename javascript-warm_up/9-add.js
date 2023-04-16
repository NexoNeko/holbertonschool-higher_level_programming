#!/usr/bin/node

function add (a, b) {
  return a + b;
}

const result = add(Number(process.argv[2]), Number(process.argv[3]));
console.log(result);
