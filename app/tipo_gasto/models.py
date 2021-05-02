from django.db import models
from django.forms import model_to_dict


class tipo_gasto(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return '%s' % self.nombre

    def get_full_name(self):
        return '{}'.format(self.nombre)

    def toJSON(self):
        item = model_to_dict(self)
        item['full'] = self.get_full_name()
        return item

    class Meta:
        db_table = 'tipo_gasto'
        verbose_name = 'tipo_gasto'
        verbose_name_plural = 'tipo_gastos'
        ordering = ['-id', '-nombre']