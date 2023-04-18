#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const _website = process.argv[2];
const _filePath = process.argv[3];

request(_website, function (error, response, body) {
  if (error) {
    console.log('error:', error);
  }
  fs.writeFile(_filePath, body, err => {
    if (err) {
      console.error(err);
    }
  });
});
