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

            marca: {
                required: true,
                // minlength: 10,
                //maxlength: 10,
                //digits: true
            },
            modelo: {
                required: true,
                // minlength: 10,
                //maxlength: 10,
                //digits: true
            },
            descripcion: {
                required: true,
               // minlength: 10,
                //maxlength: 10,
                //digits: true
            },
            pvp: {
                required: true,
               // minlength: 10,
                //maxlength: 10,
                //digits: true
            },

        },
        messages: {
            nombre: {
                required: "Porfavor ingresar un nombre para el cargo",
                minlength: "Debe ingresar al menos tres letras de tu cargo",
                lettersonly: "Debe ingresar unicamente letras y espacios"
            },
            marca: {
                required: "Porfavor escoja una marca",
                //   minlength: "El suedo debe tener al menos  1 digito",
                //digits: "Debe ingresar unicamente numeros",
                // maxlength: "El sueldo maximo 5 digitos",
            },
            modelo: {
                required: "Porfavor escoja un modelo",
                //   minlength: "El suedo debe tener al menos  1 digito",
                //digits: "Debe ingresar unicamente numeros",
                // maxlength: "El sueldo maximo 5 digitos",
            },
            descripcion: {
                required: "Porfavor realize una breve descripcion",
                //   minlength: "El suedo debe tener al menos  1 digito",
                //digits: "Debe ingresar unicamente numeros",
                // maxlength: "El sueldo maximo 5 digitos",
            },
            pvp: {
                required: "Porfavor el precio de venta",
                //   minlength: "El suedo debe tener al menos  1 digito",
                //digits: "Debe ingresar unicamente numeros",
                // maxlength: "El sueldo maximo 5 digitos",
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