async function getNameJSON() {
	const response = await fetch("https://swapi-api.hbtn.io/api/people/5/?format=json");
	const jsonData = await response.json();
	document.getElementById('character').innerHTML = jsonData.name;
}

window.addEventListener("load", (event) => {
	getNameJSON()
});