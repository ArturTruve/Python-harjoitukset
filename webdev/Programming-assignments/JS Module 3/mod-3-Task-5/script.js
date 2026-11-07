"use strict";

let numbers = [];

let input = prompt("Give a number:");
let num = Number(input);

while (numbers.includes(num) == false) {
    numbers.push(num);
    input = prompt("Give a number:");
    num = Number(input);
}

alert("The number you gave is already on the list");

numbers.sort((a, b) => a - b);

for (let i=0; i < numbers.length; i++) {
    console.log(numbers[i]);
}