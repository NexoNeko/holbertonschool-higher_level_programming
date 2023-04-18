const character = document.querySelector('character');
const updateHeader = document.querySelector('#update_header');
const request = require('request');


updateHeader.addEventListener('click', () => {
	const film = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
	request(film, function (error, response, body) {
	  if (error) {
		console.log('error:', error);
	  }
	  console.log(response);
	  character.innerText = JSON.stringify(body.name);
	});
});

