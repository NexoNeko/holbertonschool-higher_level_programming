#!/usr/bin/node

const request = require('request');
const film = process.argv[2];

request(film, function (error, response, body) {
  if (error) {
    console.log('error:', error);
  }
  const x = JSON.stringify(body);
  console.log(x.match(/people\/18\//g).length);
});
