import { BASE_URL_API } from '../config.js';

function getMedicamentos(){
    console.log('INICIANDO REQUEST A LA API...');
    var xhr = new XMLHttpRequest();
    xhr.withCredentials = true;

    xhr.addEventListener("readystatechange", function() {
    if(this.readyState === 4) {
        console.log(this.responseText);
    }
    });

    xhr.open("GET", BASE_URL_API+"medicamentos/");

    xhr.send();
}

//Carga los datos automáticamente al iniciar la vista
//window.onload = getMedicamentos();


export function deleteMedicamento(id){
    console.log('INICIANDO REQUEST A LA API...');

    urlDelete = BASE_URL_API + 'medicamento/' + id
    
    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");

    var requestOptions = {
    method: 'DELETE',
    headers: myHeaders,
    redirect: 'follow'
    };

    fetch(urlDelete, requestOptions)
    .then(response => response.text())
    .then(result => console.log(result))
    .catch(error => console.log('error', error));
}