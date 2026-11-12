"use strict";

const items = ["First item", "Second item", "Third item"];

const target = document.querySelector("#target");

target.innerHTML = items.map(item => `<li>${item}</li>`).join("");

target.classList.add("my-list");