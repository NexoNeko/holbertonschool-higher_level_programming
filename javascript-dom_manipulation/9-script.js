window.addEventListener("DOMContentLoaded", (event) => {
	const myList = document.querySelector("ul.my_list");
	const addItem = document.getElementById('add_item');
	const removeItem = document.getElementById('remove_item');
	const clearList = document.getElementById('clear_list');

	addItem.addEventListener('click', function () {
		const newLi = document.createElement('li');
		newLi.appendChild(document.createTextNode('Item'));
		myList.appendChild(newLi);
	});

	removeItem.addEventListener('click', function () {
		const lastLi = myList.lastElementChild;
		if (lastLi) {
		  myList.removeChild(lastLi);
		}
	});

	clearList.addEventListener('click', function () {
		myList.innerHTML = '';
	});
});
