"use strict";

const items = ["First item", "Second item", "Third item"];

const target = document.querySelector("#target");

for (const itemi of items) {
    const item = document.createElement("li");
    item.innerText = itemi;
    target.appendChild(item);
};

const itemList = document.querySelectorAll("#target li");

itemList[1].classList.add("my-item");