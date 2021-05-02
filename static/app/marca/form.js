$(document).ready(function () {
   validar_stilo();
    $("#form").validate({
        rules: {
            nombre: {
                required: true,
                minlength: 3,
                maxlength: 50,
                lettersonly: true,
            },

        },
        messages: {
            nombre: {
                required: "Porfavor ingresar un nombre para el cargo",
                minlength: "Debe ingresar al menos tres letras de tu cargo",
                lettersonly: "Debe ingresar unicamente letras y espacios"
            },
            sueldo: {
               required: "Porfavor ingresa un sueldo",
            //   minlength: "El suedo debe tener al menos  1 digito",
               //digits: "Debe ingresar unicamente numeros",
               // maxlength: "El sueldo maximo 5 digitos",
            },

        },
    });

     $("#formmarca").validate({
        rules: {
            nombre: {
                required: true,
                minlength: 3,
                maxlength: 50,
                lettersonly: true,
            },

        },
        messages: {
            nombre: {
                required: "Porfavor ingresar un nombre para la marca",
                minlength: "Debe ingresar al menos tres letras para la marca",
                lettersonly: "Debe ingresar unicamente letras y espacios"
            },

        },
    });

    $('#id_nombre').keyup(function () {
        var changue = $(this).val().replace(/\b\w/g, function (l) {
            return l.toUpperCase()
        });
        $(this).val(changue);
    });

});