$(document).ready(function () {
    validar_stilo();
    $("#form").validate({
        rules: {
            first_name: {
                required: true,
                minlength: 4,
                maxlength: 50,
                lettersonly: true,
            },
            last_name: {
                required: true,
                minlength: 4,
                maxlength: 50,
                lettersonly: true,
            },
            username: {
                required: true,
                minlength: 5,
                maxlength: 50,
                lettersonly: true,

            },
            email: {
                required: true,
                email: true,

            },
            password: {
                required: true,

            },
            telefono: {
                required: true,
                minlength: 10,
                maxlength: 10,
                digits: true
            },
            direccion: {
                required: true,
                minlength: 7,
                maxlength: 100,
            },
        },
        messages: {
            first_name: {
                required: "Porfavor ingresar sus nombres",
                minlength: "Debe ingresar al menos tres letras de tu cargo",
                lettersonly: "Debe ingresar unicamente letras y espacios"
            },
             last_name: {
                required: "Porfavor ingresar sus apellidos",
                minlength: "Debe ingresar al menos tres letras de tu cargo",
                lettersonly: "Debe ingresar unicamente letras y espacios"
            },
              username: {
                required: "Porfavor ingresar un username",
                minlength: "Debe ingresar al menos 5 caracteres su username",
                lettersonly: "Debe ingresar unicamente letras y espacios"
            },
             email: {
                required: "Porfavor ingresar un correo electronico",
                 email:"Porfavor ingrese un correo valido"

            },
            password: {
                required: "Porfavor ingresar una contraseña",

            },
            telefono: {
                required: "Porfavor ingresar un numero de telefono",
                //minlength: "Debe ingresar al menos tres letras de tu cargo",
                digits: 'Porfavor ingresar solo numeros '
                //lettersonly: "Debe ingresar unicamente letras y espacios"
            },
            direccion: {
                required: "Porfavor ingrese una direccion",
                minlength: "Debe ingresar al menos siete letras de su direccion",
                lettersonly: "Debe ingresar unicamente letras y espacios"
            },

        },
    });

    $('#id_first_name').keyup(function () {
        var changue = $(this).val().replace(/\b\w/g, function (l) {
            return l.toUpperCase()
        });
        $(this).val(changue);
    });
    $('#id_last_name').keyup(function () {
        var changue = $(this).val().replace(/\b\w/g, function (l) {
            return l.toUpperCase()
        });
        $(this).val(changue);
    });
    $('#id_direccion').keyup(function () {
        var changue = $(this).val().replace(/\b\w/g, function (l) {
            return l.toUpperCase()
        });
        $(this).val(changue);
    });
    $('.select2').select2({
        theme: "bootstrap4",
        language: 'es'
    });

});