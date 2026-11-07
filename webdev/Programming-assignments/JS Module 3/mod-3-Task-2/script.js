"use strict";

let list = [];

const amount = parseInt(prompt("Number of participants:"));

for (let i = 0; i < amount; i++) {
    let name = prompt(`Enter the name of participant ${i + 1}:`);
    if (name) {
        list.push(name);
    }
}

list.sort((a, b) => a.localeCompare(b));

let ol = document.getElementById("name-list");

for(let i = 0; i < list.length; i++) {
    let li = document.createElement("li");
    li.textContent = list[i];
    ol.appendChild(li);
}