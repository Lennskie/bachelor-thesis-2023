"use strict"


document.addEventListener('DOMContentLoaded', init);


function init()
{
    addList();
}

function addList(){
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
                removeEntry(data[i].uuid)
            });
            listItem.appendChild(button);
            const ul = document.querySelector('ul');
            ul.appendChild(listItem);
        }
    });
}

function removeEntry(uuid){
    console.log(uuid);
}
