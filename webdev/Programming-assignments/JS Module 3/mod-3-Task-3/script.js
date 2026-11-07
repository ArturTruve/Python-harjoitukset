"use strict";

let dogs = [];

dogs[0] = prompt("Give the first dog's name: ");
dogs[1] = prompt("Give the second dog's name: ");
dogs[2] = prompt("Give the third dog's name: ");
dogs[3] = prompt("Give the fourth dog's name: ");
dogs[4] = prompt("Give the fifth dog's name: ");
dogs[5] = prompt("Give the sixth dog's name: ");

dogs.sort((a, b) => b.localeCompare(a));

let dogList = document.getElementById("dog-list");

for (let i = 0; i < dogs.length; i++) {
  let listItem = document.createElement("li");
  listItem.textContent = dogs[i];
  dogList.appendChild(listItem);
}