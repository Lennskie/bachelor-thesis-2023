"use strict"


document.addEventListener('DOMContentLoaded', init);
function init(){
    addList();
}

function addList(){
    // read from files.json which is in the root directory and select the first element
    fetch('../files.json')
    .then(response => response.json())
    .then(data => {
        for (let i = 0; i < 5; i++) {
            document.querySelector('ul').innerHTML += `<li>Dir: ${data[i].path} ; last opened at: ${data[i].last_access_time} & opened_status: ${data[i].accessed}</li>`
        }
    });
 
}