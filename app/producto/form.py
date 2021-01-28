from django import forms
from datetime import *
from django.forms import SelectDateWidget, TextInput, NumberInput, EmailInput
from .models import producto
class productoForm(forms.ModelForm):
    # constructor
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        this_year = datetime.now().year
        years = range(this_year - 15, this_year - 3)
        for field in self.Meta.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
            self.fields['nombre'].widget = TextInput(
                attrs={'placeholder': 'Ingrese el nombre', 'class': 'form-control form-rounded','autocomplete': 'off'})
            self.fields['descripcion'].widget = TextInput(
                attrs={'placeholder': 'Ingrese una descripcion', 'class': 'form-control form-rounded','autocomplete': 'off'})
            self.fields['pvp'].widget = TextInput(
                attrs={'placeholder': 'Ingrese el pvp', 'class': 'form-control form-rounded','autocomplete': 'off'})
            self.fields['stock'].widget = TextInput(
                attrs={'placeholder': 'Ingrese el stock', 'class': 'form-control form-rounded','autocomplete': 'off'})

        # habilitar, desabilitar, y mas

    class Meta:
        model = producto
        fields = ['nombre',
                  'marca',
                  'modelo',
                  'descripcion',
                  'pvp',
                  'stock',
                  ]
        labels = {
            'nombre': 'Nombre',
            'marca': 'Marca',
            'modelo': 'Modelo',
            'descripcion': 'Descripcion',
            'pvp': 'Pvp',
            'stock': 'Stock',

        }
        widgets = {
            'nombre': forms.TextInput(),
            'marca': forms.Select(attrs={'class': 'selectpicker', 'data-width': 'fit'}),
            'modelo': forms.Select(attrs={'class': 'selectpicker', 'data-width': 'fit'}),
            'descripcion': forms.TextInput(),
            'pvp': forms.TextInput(),
            'stock': forms.TextInput(),
        }
