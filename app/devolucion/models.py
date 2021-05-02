from datetime import datetime

from django.db import models
from django.forms import model_to_dict

from app.venta.models import venta


class devolucion(models.Model):
    venta = models.ForeignKey(venta, on_delete=models.PROTECT, null=True, blank=True)
    fecha = models.DateField(default=datetime.now)

    def __str__(self):
        return '%s' % self.venta.id

    def toJSON(self):
        item = model_to_dict(self)
        item['venta'] = self.venta.toJSON()
        item['fecha'] = self.fecha.strftime('%Y-%m-%d')
        return item

    class Meta:
        db_table = 'devolucion'
        verbose_name = 'devolucion'
        verbose_name_plural = 'devoluciones'
        ordering = ['-id']