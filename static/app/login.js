$(function () {
    $('#formlogin').on('submit', function (e) {

        e.preventDefault();

        if ($('input[name="username"]').val() === "") {
            menssaje_error('Error!', "Debe ingresar un Username", 'far fa-times-circle');
            return false
        } else if ($('input[name="password"]').val() === "") {
            menssaje_error('Error!', "Debe ingresar una contraseña", 'far fa-times-circle');
            return false
        }
        var parametros;
        parametros = {
            'username': $('input[name="username"]').val(),
            'password': $('input[name="password"]').val()
        };
        login('/login/connect/', parametros, function () {
            // window.$.dialog({
            //     icon: 'fa fa-spinner fa-spin',
            //     title: 'Iniciando Sesion!',
            //     content: false
            // });
            // setTimeout(function () {
            //     location.href = '/';
            // }, 2000);
            let timerInterval
            Swal.fire({
                title: 'Iniciando Sesion!',
                timer: 2000,
                timerProgressBar: true,
                didOpen: () => {
                    Swal.showLoading()
                },
                willClose: () => {
                    clearInterval(timerInterval)
                }
            }).then((result) => {
                /* Read more about handling dismissals below */
                if (result.dismiss === Swal.DismissReason.timer) {
                    console.log('I was closed by the timer')
                }
            })
            setTimeout(function () {
                location.href = '/dashbord';
            }, 2000);

        });
    });
});

