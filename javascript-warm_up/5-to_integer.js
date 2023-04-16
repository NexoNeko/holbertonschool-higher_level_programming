#!/usr/bin/node

let inputValue = Math.floor(Number(process.argv[2]));
console.log(isNaN(inputValue) ? 'Not a number' : `My number: ${inputValue}`);
