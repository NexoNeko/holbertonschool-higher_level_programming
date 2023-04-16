#!/usr/bin/node

let args = process.argv.map(Number)
    .slice(2, process.argv.length)

console.log(args.sort((a, b) => a - b).slice(-2, -1));
