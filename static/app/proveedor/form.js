$(document).ready(function () {
   validar_stilo();
    $("#form").validate({
        rules: {
            razon_social: {
                required: true,
                minlength: 3,
                maxlength: 50,
                lettersonly: true,
            },
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
            razon_social: {
                required: "Porfavor ingresa la razon social de la empresa",
                minlength: "Debe ingresar al menos tres letras de tu nombre",
                lettersonly: "Debe ingresar unicamente letras y espacios"
            },
            nombres: {
                required: "Porfavor ingresa tus nombres",
                minlength: "Debe ingresar al menos tres letras de tu nombre",
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

    $("#formproveedor").validate({
        rules: {
            razon_social: {
                required: true,
                minlength: 3,
                maxlength: 50,
                lettersonly: true,
            },
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
            razon_social: {
                required: "Porfavor ingresa la razon social de la empresa",
                minlength: "Debe ingresar al menos tres letras de tu nombre",
                lettersonly: "Debe ingresar unicamente letras y espacios"
            },
            nombres: {
                required: "Porfavor ingresa tus nombres",
                minlength: "Debe ingresar al menos tres letras de tu nombre",
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
    });

});