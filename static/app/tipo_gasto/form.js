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
                required: "Porfavor ingresar un nombre para el tipo de gasto",
                minlength: "Debe ingresar al menos tres letras de tu gasto",
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