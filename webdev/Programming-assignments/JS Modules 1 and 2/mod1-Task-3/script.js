"use strict";

let sum = 0;
let product = 0;
let average = 0;

const int1 = prompt("first integer");
const int2 = prompt("second integer");
const int3 = prompt("third integer");

let int1stg, int2stg, int3stg;

int1stg = parseInt(int1);
int2stg = parseInt(int2);
int3stg = parseInt(int3);

sum = int1stg + int2stg + int3stg;
product = int1stg * int2stg * int3stg;
average = (int1stg + int2stg + int3stg) / 3;

document.querySelector("#target").innerHTML = 
"sum: " + sum;

document.querySelector("#target2").innerHTML = 
"product: " + product;

document.querySelector("#target3").innerHTML = 
"average: " + average;