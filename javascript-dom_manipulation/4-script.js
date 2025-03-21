document.addEventListener('DOMContentLoaded', function () {
  const addItem = document.getElementById('add_item');

  addItem.addEventListener('click', function () {
    console.log('clicked');
    const list = document.getElementsByClassName('my_list')[0];
    const element = document.createElement('li');

    const text = document.createTextNode('Item');
    element.appendChild(text);
    list.appendChild(element);
  });
});
