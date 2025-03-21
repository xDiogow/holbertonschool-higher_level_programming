document.addEventListener('DOMContentLoaded', function () {
  const character = document.getElementById('character');

  fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
    .then(response => response.json())
    .then(json => { character.innerHTML = json.name; });
});
