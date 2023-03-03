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
        const dataArray = Object.values(data); // convert object to array
        for(let i = 0; i < dataArray.length; i++) {
            document.querySelector('ul').innerHTML += `<li>Dir: ${data[i].path} ; last opened at: ${data[i].last_access_time} & opened_status: ${data[i].accessed}</li> <button data-uuid=${data[i].uuid}>click</button>`
        }
    });
    addButtonListeners();
}

function addButtonListeners(){
    let buttons = document.querySelectorAll('button')
    buttons.forEach(button => { addEventListener('click', () => { console.log(button.dataset.uuid) }) })
}

