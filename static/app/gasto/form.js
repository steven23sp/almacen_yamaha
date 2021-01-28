$(document).ready(function () {
    validar_stilo();
    $("#form").validate({
        rules: {
            detalle: {
                required: true,
                minlength: 3,
                maxlength: 50,
                lettersonly: true,
            },

            valor: {
                required: true,

            },
        },
        messages: {
            detalle: {
                required: "Porfavor ingrese un detalle para el gasto",
                minlength: "Debe ingresar al menos tres letras de tu gasto",
                lettersonly: "Debe ingresar unicamente letras y espacios"
            },
        },
    });

    $('#id_detalle').keyup(function () {
        var changue = $(this).val().replace(/\b\w/g, function (l) {
            return l.toUpperCase()
        });
        $(this).val(changue);
    });
    $('.select2').select2({
        theme: "bootstrap4",
        language: 'es'
    });

    $('#fecha').datetimepicker({
        format: 'YYYY-MM-DD',
        date: moment().format("YYYY-MM-DD"),
        locale: 'es',
        maxDate: moment().format("YYYY-MM-DD"),
        minDate: moment().format("YYYY-MM-DD"),

    });
});