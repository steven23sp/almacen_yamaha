$(function () {
    $('#example1').DataTable({
        responsive: true,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {
                'action' : 'busqueda'
            }, // parametros
            dataSrc: ""
        },
        columns: [
            {"data": "nombres"},
            {"data": "numero_doc"},
            {"data": "correo"},
            {"data": "telefono"},
            {"data": "direccion"},
            {"data": "direccion"},

        ],
        columnDefs: [
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    return data;
                }
            },
        ],
        initComplete: function (settings, json) {
            alert('Tabla Cargada')


        }
    });
});