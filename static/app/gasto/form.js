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

       // agregar marca modal envento click boton
    $('#btnaddtipogasto').on('click', function () {
        //presentar modal de proveedor
        $('#mymodaltipogasto').modal('show');
    });

    $('#formtipogasto').on('submit', function (e) {
        e.preventDefault();
        var parameters = new FormData(this);
        var isvalid = $(this).valid();
        if (isvalid) {
            parameters.append('action', 'add_tipo_gasto');
            submit_with_ajax('/tipo_gasto/crear/', 'Notificación', '¿Estas seguro de realizar la siguiente acción?', parameters, function (response) {

                $('#mymodaltipogasto').modal('hide');
                var newOption = new Option(response.tipo_gasto['full'], response.tipo_gasto['id'], false, true);
                $('select[name="tipo_gasto"]').append(newOption).trigger('change');
            });
        }

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

     //buscar tipo de gasto
    $('select[name="tipo_gasto"]').select2({
        theme: "bootstrap4",
        language: 'es',
        allowClear: true,
        ajax: {
            delay: 250,
            type: 'POST',
            url: window.location.pathname,
            data: function (params) {
                var queryParameters = {
                    term: params.term,
                    action: 'search_tipo_gasto'
                }
                return queryParameters;
            },
            processResults: function (data) {
                return {
                    results: data

                };
            },
        },
        placeholder: 'Ingrese una descripción',
        minimumInputLength: 1,
    });

});