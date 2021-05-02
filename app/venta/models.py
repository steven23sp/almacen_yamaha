from datetime import datetime
from django.db import models
from django.forms import model_to_dict

from app.cliente.models import cliente
from app.empleado.models import empleado
from app.producto.models import producto
from app.empresa.models import empresa

estado = (
    (0, 'DEVUELTA'),
    (1, 'FINALIZADA')
)


class venta(models.Model):
    cliente = models.ForeignKey(cliente, on_delete=models.PROTECT)
    fecha_venta = models.DateField(default=datetime.now)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    iva = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    total = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    estado = models.IntegerField(choices=estado, default=1)

    def __str__(self):
        return '%s %s %s' % (self.cliente, self.fecha_venta, self.total)

    def toJSON(self):
        item = model_to_dict(self)
        item['cliente'] = self.cliente.toJSON()
        item['subtotal'] = format(self.subtotal, '.2f')
        item['iva'] = format(self.iva, '.2f')
        item['total'] = format(self.total, '.2f')
        item['estado'] = self.get_estado_display()
        return item

    class Meta:
        db_table = 'venta'
        verbose_name = 'venta'
        verbose_name_plural = 'ventas'
        ordering = ['fecha_venta']
#


class detalle_venta(models.Model):
    venta = models.ForeignKey(venta, on_delete=models.PROTECT)
    producto = models.ForeignKey(producto, on_delete=models.PROTECT, null=True, blank=True, default=None)
    pvp = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, blank=True, null=True)
    p_venta_actual = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, blank=True, null=True)
    cantidad = models.IntegerField(default=0)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return '%s' % (self.venta)

    def toJSON(self):
        #empresa = empresa.objects.get(pk=1)
        item = model_to_dict(self)
        item['venta'] = self.venta.toJSON()
        item['producto'] = self.producto.toJSON()
        return item

    class Meta:
        db_table = 'detalle_venta'
        verbose_name = 'detalle_venta'
        verbose_name_plural = 'detalles_ventas'