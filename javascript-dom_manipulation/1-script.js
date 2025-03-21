document.addEventListener('DOMContentLoaded', function () {
  const redHeader = document.getElementById('red_header');

  redHeader.addEventListener('click', function () {
    redHeader.style.color = 'red';
  });
});
