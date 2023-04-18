const addItem = document.getElementById('add_item');
const myList = document.querySelector('.my_list');

addItem.addEventListener('click', () => {
	const newItem = document.createElement('li');
	newItem.appendChild(document.createTextNode('Item'));
	myList.appendChild(newItem);
});
