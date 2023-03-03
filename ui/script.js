"use strict"

document.addEventListener('DOMContentLoaded', init);
function init(){
    addList();
}

function addList(){
    fetch('../files.json')
        .then((response) => response.json())
        .then((json) => console.log(json));
    document.querySelector("ul").innerHTML += "<li>Item 1</li>";
}