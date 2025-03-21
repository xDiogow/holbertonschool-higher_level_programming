document.addEventListener('DOMContentLoaded', function () {
  const list = document.getElementById('list_movies');

  fetch('https://swapi-api.hbtn.io/api/films/?format=json')
    .then(response => response.json())
    .then(data => {
      const results = data.results;
      for (const item of results) {
        const movieName = document.createElement('li');
        movieName.textContent = item.title;
        list.appendChild(movieName);
      }
    });
});
