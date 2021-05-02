from django.forms import *

from app.compra.models import compra
from app.inventario.models import inventario


class inventarioForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.Meta.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
            self.fields['compra'].widget = Select(
                attrs={'placeholder': 'Busca una compra', 'class': 'form-control'})
            self.fields['compra'].queryset = compra.objects.filter(inventario_estado=0)

    class Meta:
        model = inventario
        fields = ['compra', 'ubicacion']
        widgets = {
            'compra': Select(),
            'ubicacion': Select(),
        }
