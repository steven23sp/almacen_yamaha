from django.db import models
from django.forms import model_to_dict

from app.marca.models import marca
from app.modelo.models import modelo


class producto(models.Model):
    nombre = models.CharField(max_length=50)
    marca = models.ForeignKey(marca, on_delete=models.PROTECT, null=True, blank=True)
    modelo = models.ForeignKey(modelo, on_delete=models.PROTECT, null=True, blank=True)
    descripcion = models.CharField(max_length=100)
    pvp = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, null=True, blank=True)
    stock = models.IntegerField(default=0)

    def __str__(self):
        return '%s' % (self.nombre)

    def toJSON(self):
        item = model_to_dict(self)
        item['marca'] = self.marca.toJSON()
        item['modelo'] = self.modelo.toJSON()
        item['pvp'] = format(self.pvp, '.2f')
        return item

    class Meta:
        db_table = 'producto'
        verbose_name = 'producto'
        verbose_name_plural = 'productos'
        ordering = ['-id']

