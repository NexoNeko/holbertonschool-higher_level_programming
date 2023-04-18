async function getNameJSON() {
	const response = await fetch("https://hellosalut.stefanbohacek.dev/?lang=fr");
	const jsonData = await response.json();

	const data = jsonData.hello;
	document.getElementById('hello').innerHTML = data;
}

window.addEventListener("load", (event) => {
	getNameJSON()
});

