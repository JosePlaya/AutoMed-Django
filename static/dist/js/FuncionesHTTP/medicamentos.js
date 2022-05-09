import { BASE_URL_API } from 'config.js';

$(document).ready(function() {
    console.log('INICIANDO REQUEST A LA API...');
    var settings = {
        "url": BASE_URL_API,
        "method": "GET",
        "timeout": 0,
      };
      
      $.ajax(settings).done(function (response) {
        console.log(response);
      });
    $('#medicamentos').DataTable({
        language: {
            "lengthMenu": "Mostrar _MENU_ registros",
            "zeroRecords": "No se encontraron resultados",
            "infoFiltered": "(filtrado de un total de _MAX_ registros)",
            "sSearch": "Buscar :",
            "sProcessing":"Procesando...",
            paginate: {
                previous:   "Previo",
                next:       "Siguiente",
            },
        },
        iDisplayLength: 50,
        responsive: "true",
        dom: 'Bfrtilp',
        "paging": true,
        "info":false,
        buttons:[]
    }); 
});