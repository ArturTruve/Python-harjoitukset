'use strict';
const students = [
  {
    name: 'John',
    id: '2345768',
  },
  {
    name: 'Paul',
    id: '2134657',
  },
  {
    name: 'Jones',
    id: '5423679',
  },
];

const target = document.querySelector("#target");

for (const i of students) {
  const item = document.createElement("option");
  item.innerText = i.name;
  item.value = i.id;
  target.appendChild(item);
};

