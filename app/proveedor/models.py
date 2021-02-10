from django.db import models
from django.forms import model_to_dict

# Create your models here.
tipo = (
    (1, 'CEDULA'),
    (0, 'RUC'),
)

class proveedor(models.Model):
    razon_social = models.CharField(max_length=50)
    nombres = models.CharField(max_length=50)
    tipo_doc = models.IntegerField(choices=tipo, default=1)
    numero_doc = models.CharField(max_length=13, unique=True)
    correo = models.CharField(max_length=50, null=True, blank=True)
    telefono = models.CharField(max_length=10)
    direccion = models.CharField(max_length=50)

    def __str__(self):
        return '%s' % self.nombres

    def get_full_name(self):
        return '{}/ {} / {}'.format(self.nombres, self.razon_social, self.numero_doc)

    def toJSON(self):
        item = model_to_dict(self)
        item['full'] = self.get_full_name()
        return item

    class Meta:
        db_table = 'proveedor'
        verbose_name = 'proveedor'
        verbose_name_plural = 'proveedores'
        ordering = ['-nombres', '-numero_doc']
