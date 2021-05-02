from datetime import datetime

from django.db import models
from django.forms import model_to_dict

from app.compra.models import compra
from app.producto.models import producto
from app.venta.models import venta
from app.ubicacion.models import ubicacion

ESTADO = (
    (1, 'En stock'),
    (0, 'Vendido'),
)
SELECT = (
    (1, 'Si'),
    (0, 'No'),
)


class inventario(models.Model):
    compra = models.ForeignKey(compra, on_delete=models.PROTECT)
    producto = models.ForeignKey(producto, on_delete=models.PROTECT, null=True, blank=True)
    estado = models.IntegerField(choices=ESTADO, default=1)
    ubicacion = models.ForeignKey(ubicacion, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return '%s' % self.producto.nombre

    def toJSON(self):
        item = model_to_dict(self)
        item['compra'] = self.compra.toJSON()
        item['producto'] = self.producto.toJSON()
        item['estado'] = self.get_estado_display()
        return item

    class Meta:
        db_table = 'inventario'
        verbose_name = 'inventario'
        verbose_name_plural = 'inventarios'
        ordering = ['-id']