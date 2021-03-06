from django.forms import *
from app.venta.models import *

class ventaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cliente'].widget.attrs['autofocus'] = True
        self.fields['cliente'].queryset = cliente.objects.none()

    class Meta:
        model = venta
        fields = '__all__'
        widgets = {
            'cliente': Select(attrs={
                'class': 'form-control select2',


            }),
            'fecha_venta': DateInput(format='%Y-%m-%d',
                                     attrs={
                                         'autocomplete': 'off',
                                         'readonly': True,
                                         'class': 'form-control datetimepicker-input',
                                         'value': datetime.now().strftime('%Y-%m-%d'),
                                         'id': 'fecha_venta',
                                         'data-target': '#fecha_venta',
                                         'data-toggle': 'datetimepicker'
                                            }),


            'subtotal': TextInput(attrs={
                'readonly': True,
                'class': 'form-control',
                'sytle': 'with 100%',

            }),
            'iva': TextInput(attrs={
                'class': 'form-control',
                'sytle': 'with 100%',

            }),
            'total': TextInput(attrs={
                'readonly': True,
                'class': 'form-control',
                'sytle': 'with 100%',

            }),
            'estado': Select(attrs={
                'class': 'form-control select2',
                'sytle': 'with 100%',

            }),
        }
