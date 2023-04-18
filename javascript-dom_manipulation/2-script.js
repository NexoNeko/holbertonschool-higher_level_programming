const header = document.querySelector('header');
const redHeader = document.getElementById('red_header');

redHeader.addEventListener('click', function () {
  header.classList.add('red');
});
