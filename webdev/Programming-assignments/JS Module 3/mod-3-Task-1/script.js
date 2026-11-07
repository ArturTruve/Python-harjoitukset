"use strict";

const numbers = [];

numbers[0] = prompt("Give the first number: ");
numbers[1] = prompt("Give the second number: ");
numbers[2] = prompt("Give the third number: ");
numbers[3] = prompt("Give the fourth number: ");
numbers[4] = prompt("Give the fifth number: ");

for (let i = 4; i >= 0; i--) {
  console.log(`for: ${numbers[i]}`);
}