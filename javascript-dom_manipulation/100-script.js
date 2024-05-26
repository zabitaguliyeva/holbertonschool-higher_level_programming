document.addEventListener('DOMContentLoaded', () => {
  const addItemButton = document.getElementById('add_item');
  const removeItemButton = document.getElementById('remove_item');
  const clearListButton = document.getElementById('clear_list');
  const myList = document.querySelector('.my_list');

  addItemButton.addEventListener('click', () => {
    const newItem = document.createElement('li');
    newItem.textContent = 'Item';
    myList.appendChild(newItem);
  });

  removeItemButton.addEventListener('click', () => {
    const lastItem = myList.lastElementChild;
    if (lastItem) {
      myList.removeChild(lastItem);
    }
  });

  clearListButton.addEventListener('click', () => {
    myList.innerHTML = '';
  });
});
