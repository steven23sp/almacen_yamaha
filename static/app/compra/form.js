var datatable;
var compras = {
    items: {
        proveedor: '',
        cantidad: '',
        pvp: '',
        fecha_compra: '',
        subtotal: 0.00,
        iva: 0.00,
        total: 0.00,
        estado: '',
        producto: []

    },
    //agregar los productos
    add: function (item) {
        this.items.producto.push(item);
        this.items.producto = this.exclude_duplicados(this.items.producto);
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
        this.calculate();
        datatable = $('#tblProducts').DataTable({
            responsive: true,
            autoWidth: false,
            destroy: true,
            dom: 'ltip',
            data: this.items.producto,
            columns: [
                {"data": "id"},
                {"data": "nombre"},
                {"data": "marca.nombre"},
                {"data": "modelo.nombre"},
                {"data": "cantidad"},
                {"data": "pvp"},
                {"data": "subtotal"},
            ],
            columnDefs: [
                {
                    targets: [0],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<a rel="remove" class="btn btn-danger btn-xs btn-flat" style="color: white"><i class="fas fa-trash-alt"></i></a>';
                    }
                },
                {
                    targets: [-2],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '$' + parseFloat(data).toFixed(2);
                    }
                },
                {
                    targets: [-3],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="cant" class="form-control form-control-sm " autocomplete="off" value="' + row.cant + '">';
                    }
                },
                {
                    targets: [-1],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '$' + parseFloat(data).toFixed(2);
                    }
                },
            ],
            rowCallback: function (row, data) {
                $(row).find('input[name="cant"]').TouchSpin({
                    min: 1,
                    max: 1000000000,
                    step: 1
                });
            }
        });
    },
    exclude_duplicados: function (array) {
        this.items.producto = [];
        let hash = {};
        result = array.filter(o => hash[o.id] ? false : hash[o.id] = true);
        return result;

    }
};
$(function () {
    compras.list();
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

    $('input[name="search"]').autocomplete({
        source: function (request, response) {
            $.ajax({
                url: window.location.pathname,
                type: 'POST',
                data: {
                    'action': 'search_products',
                    'term': request.term
                },
                dataType: 'json',
            }).done(function (data) {
                console.log(data);
                response(data);
            }).fail(function (jqXHR, textStatus, errorThrown) {
                //alert(textStatus + ': ' + errorThrown);
            }).always(function (data) {

            });
        },
        delay: 500,
        minLength: 1,
        select: function (event, ui) {
            event.preventDefault();
            console.clear();
            ui.item.cant = 1;
            ui.item.subtotal = 0.00;
            console.log(compras.items);
            compras.add(ui.item);
            $(this).val('');
        }
    });

    // agregar proveedor modal envento click boton
    $('#btnaddproveedor').on('click', function () {
        //presentar modal de proveedor
        $('#mymodalproveedor').modal('show');
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

    //buscar cliente
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
    });

    $('.btnRemoveAll').on('click', function () {
        if (compras.items.producto.length === 0) return false;
        borrar_todo_alert('Alerta de Eliminación',
            'Esta seguro que desea eliminar estos productos de su detalle <br> ' +
            '<strong>CONTINUAR?</strong>', function () {
                compras.items.producto = [];
                compras.list();
            });
    });

    //eliminar productos del detalle
    $('#tblProducts tbody')
        .on('click', 'a[rel="remove"]', function () {
            var tr = datatable.cell($(this).closest('td, li')).index();
            borrar_todo_alert('Alerta de Eliminación',
                'Esta seguro que desea eliminar este producto de tu detalle <br> ' +
                '<strong>CONTINUAR?</strong>', function () {
                    compras.items.producto.splice(tr.row, 1);
                    compras.list();
                });

        })
        //calcular el subtotal
        .on('change keyup', 'input[name="cant"]', function () {
            var cantidad = parseInt($(this).val());
            var tr = datatable.cell($(this).closest('td, li')).index();
            compras.items.producto[tr.row].cantidad = cantidad;
            compras.calculate();
            $('td:eq(6)', datatable.row(tr.row).node()).html('$' + compras.items.producto[tr.row].subtotal.toFixed(2));
        });
    $('#save').on('click', function () {
        if ($('select[name="proveedor"]').val() === "") {
            menssaje_error('Error!', "Debe seleccionar un proveedor", 'far fa-times-circle');
            return false
        } else if (compras.items.producto.length === 0) {
            menssaje_error('Error!', "Debe seleccionar al menos un producto", 'far fa-times-circle');
            return false
        }
        compras.items.fecha_compra = $('input[name="fecha_compra"]').val();
        compras.items.proveedor = $('#id_proveedor option:selected').val();
        //compra.items.estado = $('#id_estado option:selected').val();
        var parameters = new FormData();
        parameters.append('action', $('input[name="action"]').val());
        parameters.append('compra', JSON.stringify(compras.items));
        submit_with_ajax(window.location.pathname, 'Notificación', '¿Estas seguro de realizar la siguiente acción?', parameters, function () {
            location.href = '/compra/lista/';
        });
    });

    compras.list();
});

