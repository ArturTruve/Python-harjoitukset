"use strict";

const trigger = document.querySelector("#trigger");

const result = document.querySelector("#target");



trigger.addEventListener("mouseenter", function() {
    result.src = "img/picB.jpg";
});

trigger.addEventListener("mouseleave", function() {
    result.src = "img/picA.jpg";
});