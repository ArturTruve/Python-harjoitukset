"use strict";

let numbers = [];

let input = prompt("Give a number or 0 to exit");
let num = Number(input);

while (num !== 0) {
    numbers.push(num);
    input = prompt("Give a number or 0 to exit");
    num = Number(input);
}

numbers.sort((a, b) => b - a);

for (let i=0; i < numbers.length; i++) {
    console.log(numbers[i]);
}