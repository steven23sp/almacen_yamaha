var datatable, ubicacion = [];
var inventario = {
    items: {
        producto: [],
        compra:''
    },
    //agregar los productos
    add: function (item) {
        this.items.producto.push(item[0]);
        console.log(inventario.items.producto);
        this.list();
    },
    //calcular
    calculate: function () {
        var subtotal = 0.00;
        $.each(this.items.producto, function (pos, dict) {
            dict.subtotal = dict.cantidad * parseFloat(dict.pvp);
            subtotal += dict.subtotal;
        });
        this.items.subtotal = subtotal;
        this.items.iva = this.items.subtotal * 0.12;
        this.items.total = this.items.subtotal + this.items.iva;
        $('input[name="subtotal"]').val(this.items.subtotal.toFixed(2));
        $('input[name="iva"]').val(this.items.iva.toFixed(2));
        $('input[name="total"]').val(this.items.total.toFixed(2));
    },
    list: function () {
        datatable = $('#tblProducts').DataTable({
            responsive: true,
            autoWidth: false,
            destroy: true,
            dom: 'ltip',
            data: this.items.producto,
            columns: [
                {"data": "producto.nombre"},
                {"data": "producto.marca.nombre"},
                {"data": "producto.modelo.nombre"},
                {"data": "cantidad"},
                {"data": "id"},
            ],
            language: {
                url: '//cdn.datatables.net/plug-ins/1.10.15/i18n/Spanish.json',
            },
            columnDefs: [
                {
                    targets: [-1],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        var select = '<select name="ubicacion" class="form-control select2">';
                            $.each(row.ubicacion, function (key, value) {
                                select += '<option value="'+value.id+'">'+value.nombre+'';
                            });
                            select += '</select>';

                        return select
                    }
                },
            ],
            // rowCallback: function (row, data) {
            //     $(row).find('input[name="cant"]').TouchSpin({
            //         min: 1,
            //         max: 1000000000,
            //         step: 1
            //     });
            // }
        });
    },
};

$(function () {
    inventario.list();
    $('.select2').select2({
        theme: "bootstrap4",
        language: 'es'
    });

    $('#fecha_compra').datetimepicker({
        format: 'YYYY-MM-DD',
        date: moment().format("YYYY-MM-DD"),
        locale: 'es',
        maxDate: moment().format("YYYY-MM-DD"),
        minDate: moment().format("YYYY-MM-DD"),

    });

    $("input[name='iva']").prop('readonly', true);


    // buscar productos

    // $('input[name="search"]').autocomplete({
    //     source: function (request, response) {
    //         $.ajax({
    //             url: window.location.pathname,
    //             type: 'POST',
    //             data: {
    //                 'action': 'search_detalle',
    //                 'id': request.term
    //             },
    //             dataType: 'json',
    //         }).done(function (data) {
    //             console.log(data);
    //             response(data);
    //         }).fail(function (jqXHR, textStatus, errorThrown) {
    //             //alert(textStatus + ': ' + errorThrown);
    //         }).always(function (data) {
    //
    //         });
    //     },
    //     delay: 500,
    //     minLength: 1,
    //     select: function (event, ui) {
    //         event.preventDefault();
    //         console.clear();
    //         ui.item.cant = 1;
    //         ui.item.subtotal = 0.00;
    //         console.log(compras.items);
    //         compras.add(ui.item);
    //         $(this).val('');
    //     }
    // });


    $('#id_compra').select2().on('select2:select', function () {
        $.ajax({
            dataType: 'JSON',
            type: 'POST',
            url: window.location.pathname,
            data: {'id': $('#id_compra option:selected').val(), 'action': 'get_det'},
        })
            .done(function (data) {
                if (!data.hasOwnProperty('error')) {
                    inventario.add(data);
                    return false;
                }
                menssaje_error('Error', data.error, 'fas fa-exclamation-circle');

            })
            .fail(function (jqXHR, textStatus, errorThrown) {
                alert(textStatus + ': ' + errorThrown);
            });
    })

    // agregar proveedor modal envento click boton
    $('#btnaddproveedor').on('click', function () {
        //presentar modal de proveedor
        $('#mymodalproveedor').modal('show');
    });

    $('#buscar_producto').on('click', function () {
        $('#tbldetalle').DataTable({
            responsive: true,
            autoWidth: false,
            destroy: true,
            deferRender: true,
            ajax: {
                url: window.location.pathname,
                type: 'POST',
                data: {
                    'action': 'detalle',
                    //'id': data.id
                },
                dataSrc: ""
            },
            language: {
                url: '//cdn.datatables.net/plug-ins/1.10.15/i18n/Spanish.json',
            },
            columns: [
                {"data": "nombre"},
                //{"data": "producto.marca"},
                //{"data": "producto.modelo"},
                {"data": "stock"},
                //{"data": "subtotal"},

            ],
            columnDefs: [

                {
                    targets: '_all',
                    class: 'text-center',

                },
            ]
        })
        $('#mymodalproducto').modal('show');
    });

    $('#formproveedor').on('submit', function (e) {
        e.preventDefault();
        var parameters = new FormData(this);
        var isvalid = $(this).valid();
        if (isvalid) {
            parameters.append('action', 'add_compra');
            submit_with_ajax('/proveedor/crear/', 'Notificación', '¿Estas seguro de realizar la siguiente acción?', parameters, function (response) {

                $('#mymodalproveedor').modal('hide');
                var newOption = new Option(response.proveedor['full'], response.proveedor['id'], false, true);
                $('select[name="proveedor"]').append(newOption).trigger('change');
            });
        }

    });

    //buscar proveedor
    $('select[name="proveedor"]').select2({
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
                    action: 'search_proveedor'
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
    })


    //eliminar productos del detalle
    $('#tblProducts tbody')
        .on('change', 'select[name="ubicacion"]', function () {
            var ubicacion = $(this).val();
            var tr = datatable.cell($(this).closest('td, li')).index();
            inventario.items.producto[tr.row].ubicacion = ubicacion;
        });
    $('#save').on('click', function () {
        inventario.items.compra = $('#id_compra option:selected').val();
        var parametros;
        parametros = {'inventario': JSON.stringify(inventario.items)};
        parametros['action'] = 'add';
        submit_with_ajax_other('/inventario/crear/', 'Notificación', '¿Estas seguro de realizar la siguiente acción?', parametros, function () {
            location.href = '/inventario/lista/';
        });
    });

    inventario.list();
});

