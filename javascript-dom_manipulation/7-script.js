async function getNameJSON() {
	const response = await fetch("https://swapi-api.hbtn.io/api/films/?format=json");
	const jsonData = await response.json();
	const myList = document.getElementById('list_movies');

	const movies = jsonData.results;
	const ul = document.getElementById('list_movies');
	for (let i = 0; i < movies.length; i++) {
	  const li = document.createElement('li');
	  li.textContent = movies[i].title;
	  ul.appendChild(li);
	}
}

window.addEventListener("load", (event) => {
	getNameJSON()
});

