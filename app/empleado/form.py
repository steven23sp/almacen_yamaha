from django import forms
from datetime import *
from django.forms import SelectDateWidget, TextInput, NumberInput, EmailInput
from .models import empleado
class empleadoForm(forms.ModelForm):
    # constructor
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        this_year = datetime.now().year
        years = range(this_year - 15, this_year - 3)
        for field in self.Meta.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
            self.fields['nombres'].widget = TextInput(
                attrs={'placeholder': 'Ingrese sus nombres', 'class': 'form-control form-rounded','autocomplete': 'off'})
            self.fields['apellidos'].widget = TextInput(
                attrs={'placeholder': 'Ingrese sus apellidos', 'class': 'form-control form-rounded','autocomplete': 'off'})
            self.fields['cedula'].widget = TextInput(
                attrs={'placeholder': 'Ingrese su numero de cedula', 'class': 'form-control form-rounded','autocomplete': 'off'})
            self.fields['edad'].widget = TextInput(
                attrs={'placeholder': 'Ingrese su edad', 'class': 'form-control form-rounded','autocomplete': 'off'})
            self.fields['correo'].widget = EmailInput(
                attrs={'placeholder': 'abc@correo.com', 'class': 'form-control form-rounded','autocomplete': 'off'})
            self.fields['telefono'].widget = TextInput(
                attrs={'placeholder': 'Ingrese el numero de celular','class': 'form-control form-rounded', 'autocomplete': 'off'})
            self.fields['direccion'].widget = TextInput(
                attrs={'placeholder': 'Ingrese su direccion con maximo 50 caracteres', 'class': 'form-control form-rounded','autocomplete': 'off'})

        # habilitar, desabilitar, y mas

    class Meta:
        model = empleado
        fields = ['nombres',
                  'apellidos',
                  'cedula',
                  'edad',
                  'correo',
                  'telefono',
                  'direccion',
                  'cargo'
                  ]
        labels = {
            'nombres': 'Nombres',
            'apellido': 'Apellidos',
            'cedula': 'Cedula',
            'edad': 'Edad',
            'correo': 'Correo',
            'telefono': 'Telefono',
            'direccion': 'Direccion',
            'cargo': 'Cargo'

        }
        widgets = {
            'nombres': forms.TextInput(),
            'apellidos': forms.TextInput(),
            'cedula': forms.TextInput(),
            'edad': forms.TextInput(),
            'correo': forms.EmailInput(),
            'telefono': forms.TextInput(),
            'direccion': forms.TextInput(),
            'cargo': forms.Select(attrs={'class': 'selectpicker', 'data-width': 'fit'}),
        }
