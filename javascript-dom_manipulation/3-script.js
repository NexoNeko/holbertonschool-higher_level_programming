const header = document.querySelector('header');
const toggleHeader = document.getElementById('toggle_header');

toggleHeader.addEventListener('click', function () {
	if (header.classList.contains('red')) {
		header.classList.remove('red');
		header.classList.add('green');
	} else if (header.classList.contains('green')) {
		header.classList.remove('green');
		header.classList.add('red');
	} else {
		header.classList.add('red');
	}
});

