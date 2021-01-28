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
                'action': 'searchdata'
            },
            dataSrc: ""
        },
         language: {
            url: '//cdn.datatables.net/plug-ins/1.10.15/i18n/Spanish.json',
        },
        columns: [
            {"data": "nombre"},
            {"data": "marca.nombre"},
            {"data": "modelo.nombre"},
            {"data": "descripcion"},
            {"data": "pvp"},
            {"data": "stock"},
            {"data": "id"},

        ],
        columnDefs: [
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var editar = '<a type="button" class="btn btn-outline-success btn-sm btn-round" data-toggle="tooltip"title="Editar Datos" href="/producto/editar/' + data + '"><i class="fa fa-edit"></i></a> ';
                    borrar = '<a type="button" class="btn btn-outline-danger btn-sm btn-round" data-toggle="tooltip" title="Eliminar Datos" rel="delete"><i class="fa fa-trash"></i></a>';
                    return editar + borrar;
                }
            },
            {
                targets: [-2],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    if (row.stock === 0)
                    {
                        return '<span class=" badge badge-danger"> '+data+'</span>'
                    }
                    else
                        if (row.stock <= 30)
                        {
                            return '<span class=" badge badge-warning"> '+data+'</span>'
                        }
                    return '<span class=" badge badge-success"> '+data+'</span>'
                }
            },
        ]
    });

    $('#example1 tbody')
        .on('click', 'a[rel="delete"]', function () {
            var tr = datatable.cell($(this).closest('td, li')).index();
            var data = datatable.row(tr.row).data();
            var parametros = {'id': data.id};
            parametros['action'] = 'delete'
            submit_with_ajax(window.location.pathname, 'Alerta de Eliminacion!',
                'Esta seguro que desea borrar este producto', parametros, function () {
                    datatable.ajax.reload(null, false);
                })
        })
});