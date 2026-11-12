'use strict';
const names = ['John', 'Paul', 'Jones'];

const target = document.querySelector("#target");

let htmlContent = "";

for (const name of names) {
    htmlContent += `<li>${name}</li>`;
};

target.innerHTML = htmlContent;