import { BASE_URL_API } from './config.js';

// $(document).ready(function() {
//     console.log('INICIANDO REQUEST A LA API...');
//     console.log(BASE_URL_API);
//     var settings = {
//         "url": BASE_URL_API+'/medicamentos',
//         "method": "GET",
//         "timeout": 0,
//       };
      
//       $.ajax(settings).done(function (response) {
//         console.log(response);
//       });
//     $('#medicamentos').DataTable({
//         language: {
//             "lengthMenu": "Mostrar _MENU_ registros",
//             "zeroRecords": "No se encontraron resultados",
//             "infoFiltered": "(filtrado de un total de _MAX_ registros)",
//             "sSearch": "Buscar :",
//             "sProcessing":"Procesando...",
//             paginate: {
//                 previous:   "Previo",
//                 next:       "Siguiente",
//             },
//         },
//         iDisplayLength: 50,
//         responsive: "true",
//         dom: 'Bfrtilp',
//         "paging": true,
//         "info":false,
//         buttons:[]
//     }); 
// });

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
window.onload = getMedicamentos();