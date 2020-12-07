from datetime import datetime
from django.db import models
from django.forms import model_to_dict

from app.producto.models import producto
#from apps.presentacion.models import presentacion
from app.proveedor.models import proveedor

estado = (
    (0, 'DEVUELTA'),
    (1, 'FINALIZADA')
)


class compra(models.Model):
    fecha_compra = models.DateField(default=datetime.now)
    proveedor = models.ForeignKey(proveedor, on_delete=models.PROTECT)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    iva = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    total = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    estado = models.IntegerField(choices=estado, default=1)

    def __str__(self):
        return '%s %s' % (self.fecha_compra, self.proveedor.nombres)

    def toJSON(self):
        item = model_to_dict(self)
        item['proveedor'] = self.proveedor.toJSON()
        item['subtotal'] = format(self.subtotal, '.2f')
        item['iva'] = format(self.iva, '.2f')
        item['total'] = format(self.total, '.2f')
        return item

    class Meta:
        db_table = 'compra'
        verbose_name = 'compra'
        verbose_name_plural = 'compras'
        ordering = ['-id', 'proveedor']


class detalle_compra(models.Model):
    compra = models.ForeignKey(compra, on_delete=models.PROTECT)
    producto = models.ForeignKey(producto, on_delete=models.PROTECT)
    cantidad = models.IntegerField(default=1)

    def __str__(self):
        return '%s %s' % (self.compra, self.producto.nombre)

    def toJSON(self):
        item = model_to_dict(self)
        item['compra'] = self.compra.toJSON()
        item['producto'] = self.producto.toJSON()
        return item

    class Meta:
        db_table = 'detalle_compra'
        verbose_name = 'detalle_compra'
        verbose_name_plural = 'detalles_compras'
        ordering = ['id', 'compra']