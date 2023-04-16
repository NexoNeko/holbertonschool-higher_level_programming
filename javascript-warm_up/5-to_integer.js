#!/usr/bin/node

const inputValue = Math.floor(Number(process.argv[2]));
console.log(isNaN(inputValue) ? 'Not a number' : `My number: ${inputValue}`);
