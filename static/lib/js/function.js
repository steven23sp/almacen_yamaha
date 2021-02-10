//function menssaje_error(obj) {
//    var html = '';
//    if (typeof (obj) === 'object') {
//        html = '<ul style="text-align: left;">';
//        $.each(obj, function (key, value) {
//            html += '<li>' + key + ': ' + value + '</li>';
//        });
//       html += '</ul>';
//    } else {
//        html = '<p>' + obj + '</p>';
//    }
//    Swal.fire({
//        title: 'Error!',
//       html: html,
//       icon: 'error'
//    });
//}

function submit_with_ajax(url, title, content, parameters, callback) {
    $.confirm({
        theme: 'material',
        title: title,
        icon: 'fa fa-info',
        content: content,
        columnClass: 'small',
        typeAnimated: true,
        cancelButtonClass: 'btn-primary',
        draggable: true,
        dragWindowBorder: false,
        buttons: {
            info: {
                text: "Si",
                btnClass: 'btn-primary',
                action: function () {
                    $.ajax({
                        dataType: 'JSON',
                        type: 'POST',
                        url: url,
                        processData: false,
                        contentType: false,
                        data: parameters,
                    }).done(function (data) {
                        if (!data.hasOwnProperty('error')) {
                            callback(data);
                            return false;
                        }
                        menssaje_error('Error', data.error, 'fas fa-exclamation-circle');

                    }).fail(function (jqXHR, textStatus, errorThrown) {
                        alert(textStatus + ': ' + errorThrown);
                    });
                }
            },
            danger: {
                text: "No",
                btnClass: 'btn-red',
                action: function () {

                }
            },
        }
    })
}


function submit_with_ajax_other(url, title, content, parameters, callback) {
    $.confirm({
        theme: 'material',
        title: title,
        icon: 'fa fa-info',
        content: content,
        columnClass: 'small',
        typeAnimated: true,
        cancelButtonClass: 'btn-primary',
        draggable: true,
        dragWindowBorder: false,
        buttons: {
            info: {
                text: "Si",
                btnClass: 'btn-primary',
                action: function () {
                    $.ajax({
                        dataType: 'JSON',
                        type: 'POST',
                        url: url,
                        data: parameters,
                    }).done(function (data) {
                        if (!data.hasOwnProperty('error')) {
                            callback(data);
                            return false;
                        }
                        menssaje_error('Error', data.error, 'fas fa-exclamation-circle');

                    }).fail(function (jqXHR, textStatus, errorThrown) {
                        alert(textStatus + ': ' + errorThrown);
                    });
                }
            },
            danger: {
                text: "No",
                btnClass: 'btn-red',
                action: function () {

                }
            },
        }
    })
}

function validar_stilo() {

    $.validator.setDefaults({
        errorClass: 'invalid-feedback',

        highlight: function (element, errorClass, validClass) {
            $(element)
                .addClass("is-invalid")
                .removeClass("is-valid");
        },
        unhighlight: function (element, errorClass, validClass) {
            $(element)
                .addClass("is-valid")
                .removeClass("is-invalid");
        }
    });
}


function borrar_todo_alert(title, content, callback) {
    $.confirm({
        title: title,
        icon: 'fas fa-exclamation-triangle',
        type: 'red',
        typeAnimated: true,
        content: content,
        draggable: true,
        buttons: {
            si: {
                text: '<i class="fas fa-check"></i> Si',
                btnClass: 'btn-blue',
                action: function () {
                    callback();
                }
            },
            no: {
                text: '<i class="fas fa-times"></i> No',
                btnClass: 'btn-red'
            },
        }
    });
}

function menssaje_error(title, content, icon, callback) {
    var obj = $.confirm({
        theme: 'modern',
        icon: icon,
        title: title,
        type: 'red',
        content: content,
        draggable: true,
        buttons: {
            info: {
                text: '<i class="fas fa-check"></i> Ok',
                btnClass: 'btn-blue'
            },
        }
    });
    setTimeout(function () {
        // some point in future.
        obj.close();
    }, 3000);
}

function menssajeok(title, content, icon, callback) {
    var obj = $.confirm({
        theme: 'supervan',
        icon: 'fa fa-smile-o',
        title: title,
        type: 'red',
        content: content,
        draggable: true,
        buttons: {
            info: {
                text: '<i class="fas fa-check"></i> Ok',
                btnClass: 'btn-blue',
                action: function () {

                }
            },
        }
    });
    setTimeout(function () {
        // some point in future.
        obj.close();
    }, 3000);
}

function printpdf(title, content, callback, cancel) {
    $.confirm({
            theme: 'modern',
            type: 'blue',
            icon: 'fas fa-exclamation-circle',
            title: title,
            content: content,
            columnClass: 'small',
            draggable: true,
            buttons: {
                si: {
                    text: '<i class="fas fa-check"></i> Si',
                    btnClass: 'btn-blue',
                    action: function () {
                        callback();
                    }
                },
                no: {
                    text: '<i class="fas fa-times"></i> No',
                    btnClass: 'btn-red',
                    action: function () {
                        cancel();
                    }
                }
            }
        }
    );
}