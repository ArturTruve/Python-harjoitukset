"use strict";

const pick1 = "Gryffindor";
const pick2 = "Slytherin";
const pick3 = "Huffelpuff";
const pick4 = "Ravenclaw";

const name = prompt("What's your name?")

function HatSaid(min, max) {
    return Math.floor(Math.random() * (max - min)) + min;
}

const hatpick = HatSaid(1, 5);

if (hatpick === 1) {
    document.querySelector("#target").innerHTML = name + ", you are " + pick1 + ".";
} else if (hatpick === 2) {
    document.querySelector("#target").innerHTML = name + ", you are " + pick2 + ".";
} else if (hatpick === 3) {
    document.querySelector("#target").innerHTML = name + ", you are " + pick3 + ".";
} else if (hatpick === 4) {
    document.querySelector("#target").innerHTML = name + ", you are " + pick4 + ".";
}