$(function () {
    var datatable = $('#example1').DataTable({
        responsive: true,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {
                'action': 'searchdetalle',
            },
            dataSrc: ""
        },
        language: {
            url: '//cdn.datatables.net/plug-ins/1.10.15/i18n/Spanish.json',
        },
        columns: [
            {"data": "id"},
            {"data": "fecha_compra"},
            {"data": "proveedor.nombres"},
            {"data": "subtotal"},
            {"data": "total"},

        ],
        columnDefs: [
            {
                targets: [-2, -1],
                class: 'text-center',
                render: function (data, type, row) {
                    return '$ ' + data;
                }
            },

        ]
    })
});