"use strict";

let input = prompt("Give a year to see if it is a leap year: ");
let intinput = parseInt(input);

function leapyear(year) {
    return ((year % 4 === 0) && (year % 100 !== 0)) || (year % 400 === 0);
}

let answer = leapyear(intinput);

if (answer === true) {
    document.querySelector("#target").innerHTML = 
        "The year: " + input + " is a leap year.";
} else if (answer === false) {
    document.querySelector("#target").innerHTML = 
        "The year: " + input + " is not a leap year.";
}