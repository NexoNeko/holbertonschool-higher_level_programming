#!/usr/bin/node

const request = require('request');
const film = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(film, function (error, response, body) {
  if (error) {
    console.log('error:', error);
  }
  console.log(JSON.parse(body).title);
});
