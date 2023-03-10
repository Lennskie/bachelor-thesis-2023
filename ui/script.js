"use strict"


document.addEventListener('DOMContentLoaded', init);


function init()
{
    addList();
    let buttons = document.querySelectorAll('button')
    buttons.forEach(button => { button.addEventListener('click', () => { 
        console.log(button.dataset.uuid) 
    }) });    
}

function addList(){
    // read from files.json which is in the root directory and select the first element
    fetch('../files.json')
    .then(response => response.json())
    .then(data => {
        const dataArray = Object.values(data); // convert object to array
        for(let i = 0; i < dataArray.length; i++) {
            const listItem = document.createElement('li');
            listItem.innerHTML = `Dir: ${data[i].path} ; last opened at: ${data[i].last_access_time} & opened_status: ${data[i].accessed} `;
            const button = document.createElement('button');
            button.setAttribute('data-uuid', data[i].uuid);
            button.textContent = 'remove entry';
            button.addEventListener('click', () => { 
                console.log(button.dataset.uuid) 
            });
            listItem.appendChild(button);
            const ul = document.querySelector('ul');
            ul.appendChild(listItem);
        }
    });
}


