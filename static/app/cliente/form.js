$(document).ready(function () {
    validar_stilo();
    $.validator.addMethod("tipo", function (value, element) {

        var tipo = $("#tipo_doc").val();
        if (tipo === '1') {
            return ((value.length === 10));
        } else if (tipo === '0') {
            return ((value.length === 13));
        }
    }, "");
    $("#form").validate({
        rules: {
            nombres: {
                required: true,
                minlength: 3,
                maxlength: 50,
                lettersonly: true,
            },
            numero_doc: {
                required: true,
                minlength: 10,
                maxlength: 13,
                digits: true,
                validar: true
            },
            correo: {
                required: true,
                email: true
            },
            telefono: {
                required: true,
                minlength: 10,
                maxlength: 10,
                digits: true
            },
            direccion: {
                required: true,
                minlength: 5,
                maxlength: 50
            },


        },
        messages: {
            nombres: {
                required: "Porfavor ingresa tus nombres",
                minlength: "Debe ingresar al menos tres letras de tu nombre",
                lettersonly: "Debe ingresar unicamente letras y espacios"
            },
            apellidos: {
                required: "Porfavor ingresa tus apellidos",
                minlength: "Debe ingresar al menos un apellido",
                lettersonly: "Debe ingresar unicamente letras y espacios"
            },
            numero_doc: {
                required: "Porfavor ingresa tu numero de documento",
                minlength: "Tu numero de documento debe tener al menos 10 digitos",
                digits: "Debe ingresar unicamente numeros",
                maxlength: "Tu numero de documento debe tener maximo 10 digitos",
            },
            correo: "Debe ingresar un correo valido",
            telefono: {
                required: "Porfavor ingresa tu numero celular",
                minlength: "Tu numero de documento debe tener al menos 10 digitos",
                digits: "Debe ingresar unicamente numeros",
                maxlength: "Tu numero de documento debe tener maximo 10 digitos",
            },
            direccion: {
                required: "Porfavor ingresa una direccion",
                minlength: "Ingresa al menos 5 letras",
                maxlength: "Tu direccion debe tener maximo 50 caracteres",
            },
        },
    });
    $("#formcliente").validate({
        rules: {
            nombres: {
                required: true,
                minlength: 3,
                maxlength: 50,
                lettersonly: true,
            },

            numero_doc: {
                required: true,
                minlength: 10,
                maxlength: 13,
                digits: true
            },
            correo: {
                required: true,
                email: true
            },
            telefono: {
                required: true,
                minlength: 10,
                maxlength: 10,
                digits: true
            },
            direccion: {
                required: true,
                minlength: 5,
                maxlength: 50
            },
        },
        messages: {
            nombres: {
                required: "Porfavor ingresa tus nombres",
                minlength: "Debe ingresar al menos tres letras de tu nombre",
                lettersonly: "Debe ingresar unicamente letras y espacios"
            },
            apellidos: {
                required: "Porfavor ingresa tus apellidos",
                minlength: "Debe ingresar al menos un apellido",
                lettersonly: "Debe ingresar unicamente letras y espacios"
            },
            numero_doc: {
                required: "Porfavor ingresa tu numero de documento",
                minlength: "Tu numero de documento debe tener al menos 10 digitos",
                digits: "Debe ingresar unicamente numeros",
                maxlength: "Tu numero de documento debe tener maximo 10 digitos",
            },
            correo: "Debe ingresar un correo valido",
            telefono: {
                required: "Porfavor ingresa tu numero celular",
                minlength: "Tu numero de documento debe tener al menos 10 digitos",
                digits: "Debe ingresar unicamente numeros",
                maxlength: "Tu numero de documento debe tener maximo 10 digitos",
            },
            direccion: {
                required: "Porfavor ingresa una direccion",
                minlength: "Ingresa al menos 5 letras",
                maxlength: "Tu direccion debe tener maximo 50 caracteres",
            },
        },
    });
    $('#id_nombres').keyup(function () {
        var changue = $(this).val().replace(/\b\w/g, function (l) {
            return l.toUpperCase()
        });
        $(this).val(changue);
    }).keypress(function (e) {
        if (e.which >= 48 && e.which <= 57) {
            return false;
        }
    });  //Para solo letras;

    $('#id_direccion').keyup(function () {
        var changue = $(this).val().replace(/\b\w/g, function (l) {
            return l.toUpperCase()
        });
        $(this).val(changue);
    });

});


//.keypress(function (e) {
//         if (e.which !== 8 && e.which !== 0 && (e.which < 48 || e.which > 57)) {
//             return false;
//         }
//     });//Para solo numeros