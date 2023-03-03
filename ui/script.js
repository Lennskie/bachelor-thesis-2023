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
            document.querySelector('ul').innerHTML += `<li>Dir: ${dataArray[i].path} ; last opened at: ${dataArray[i].last_access_time} & opened_status: ${dataArray[i].accessed}</li> <button>click</button>`
            document.querySelectorAll('button')[i].addEventListener('click', () => {
                console.log('clicked');
            })
        }
    });
    
}