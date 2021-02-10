var datatable;
var venta = {
    items: {
        cliente: '',
        cantidad: '',
        pvp: '',
        fecha_venta: '',
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
        var indice = $('input[name="indice"]').val();
        var subtotal = 0.00;
        $.each(this.items.producto, function (pos, dict) {
            dict.subtotal = dict.cantidad * parseFloat(dict.pvp);
            subtotal += dict.subtotal;
        });
        var iva_p = $('input[name="iva_empresa"]').val();
        this.items.subtotal = subtotal;
        this.items.iva = this.items.subtotal * iva_p / 100;
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
                console.log(data);
                $(row).find('input[name="cant"]').TouchSpin({
                    min: 1,
                    max: data.stock,
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
    venta.list();
    $('.select2').select2({
        theme: "bootstrap4",
        language: 'es'
    });

    $('#fecha_venta').datetimepicker({
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
            console.log(venta.items);
            venta.add(ui.item);
            $(this).val('');
        }
    });

    $('.btnRemoveAll').on('click', function () {
        if (venta.items.producto.length === 0) return false;
        borrar_todo_alert('Alerta de Eliminación',
            'Esta seguro que desea eliminar estos productos de su detalle <br> ' +
            '<strong>CONTINUAR?</strong>', function () {
                venta.items.producto = [];
                venta.list();
            });
    });

    //eliminar productos del detalle
    $('#tblProducts tbody')
        .on('click', 'a[rel="remove"]', function () {
            var tr = datatable.cell($(this).closest('td, li')).index();
            borrar_todo_alert('Alerta de Eliminación',
                'Esta seguro que desea eliminar este producto de tu detalle <br> ' +
                '<strong>CONTINUAR?</strong>', function () {
                    venta.items.producto.splice(tr.row, 1);
                    venta.list();
                });

        })
        //calcular el subtotal
        .on('change keyup', 'input[name="cant"]', function () {
            var cantidad = parseInt($(this).val());
            var tr = datatable.cell($(this).closest('td, li')).index();
            venta.items.producto[tr.row].cantidad = cantidad;
            venta.calculate();
            $('td:eq(6)', datatable.row(tr.row).node()).html('$' + venta.items.producto[tr.row].subtotal.toFixed(2));
        });


    $('#save').on('click', function () {
        if ($('select[name="cliente"]').val() === "") {
            menssaje_error('Error!', "Debe seleccionar un cliente", 'far fa-times-circle');
            return false
        } else if (venta.items.producto.length === 0) {
            menssaje_error('Error!', "Debe seleccionar al menos un producto", 'far fa-times-circle');
            return false
        }
        venta.items.fecha_venta = $('input[name="fecha_venta"]').val();
        venta.items.cliente = $('#id_cliente option:selected').val();
        //compra.items.estado = $('#id_estado option:selected').val();
        var parameters = new FormData();
        parameters.append('action', 'add');
        parameters.append('venta', JSON.stringify(venta.items));
        submit_with_ajax(window.location.pathname, 'Notificación', '¿Estas seguro de realizar la siguiente acción?', parameters,
            function (response) {
            printpdf('Alerta!', '¿Desea generar el comprobante en PDF?', function () {
                    window.open('/venta/printpdf/' + response['id'], '_blank');
                    location.href = '/venta//lista/';
                }, function () {
                    location.href = '/venta//lista/';
                })
        });
    });
    venta.list();
});

