#!/usr/bin/node

const argumentCount = process.argv.length;

if (argumentCount < 3) {
  console.log('No argument');
} else if (argumentCount === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
