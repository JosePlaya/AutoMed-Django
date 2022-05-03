//Funciones auxiliares
function mensajeError(caja, mensaje) {
    $("#" + caja).html(mensaje)
    $("#" + caja).fadeIn()
}

function noError(caja) {
    $("#" + caja).fadeOut()
}    

//Validar Rut Usuario
function validaRutUsuario() {
    if ($("#rutUsuario").val().trim().length == 0) {
        mensajeError("rut", "Campo obligatorio")
        return false
    } else {
        noError("rut")
        return true
    }
}

//Validar Rut Usuario
function validaPassword() {
    if ($("#passwordUsuario").val().trim().length == 0) {
        mensajeError("password", "Campo obligatorio")
        return false
    } else {
        noError("password")
        return true
    }
}


$(document).ready(function () {
     /*Configuración inicial del formulario*/

    //Todos los mensajes de error ocultos
    $(".invalid-feedback").hide();

    //Validar Rut Usuario
    $("#rutUsuario").blur(function () {
        exito = validaRutUsuario()
    });

    //Validar Password Usuario
    $("#passwordUsuario").blur(function () {
        exito = validaPassword()
    });

    //Envío del formulario
    $("#form1").submit(function () {
        exito = false

        //Validar antes de enviar formulario
        if(
            !validaRutUsuario() ||
            !validaPassword()
        ){
            event.preventDefault()
        }
    });

});