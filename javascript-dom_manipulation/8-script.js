document.addEventListener('DOMContentLoaded', () => {
  fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
    .then(response => response.json())
    .then(json => {
      const element = document.getElementById('hello');
      element.innerHTML = json.hello;
    });
});
