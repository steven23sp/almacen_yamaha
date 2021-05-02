from django.db import models
from django.forms import model_to_dict
from app.empresa.models import empresa
from app.marca.models import marca
from app.modelo.models import modelo
from sistema_yamaha.settings import MEDIA_URL, STATIC_URL


class producto(models.Model):
    nombre = models.CharField(max_length=50)
    marca = models.ForeignKey(marca, on_delete=models.PROTECT, null=True, blank=True)
    modelo = models.ForeignKey(modelo, on_delete=models.PROTECT, null=True, blank=True)
    descripcion = models.CharField(max_length=100)
    pvp = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, null=True, blank=True)
    stock = models.IntegerField(default=0)
    imagen = models.ImageField(upload_to='producto/imagen', null=True, blank=True, verbose_name='Imagen')

    def __str__(self):
        return '%s' % (self.nombre)

    def pvp_cal(self):
        ind = empresa.objects.first()
        pvp = float(self.pvp) * (1+float(ind.indice))
        return format(pvp, '.2f')

    def get_image(self):
        if self.imagen:
            return '{}{}'.format(MEDIA_URL, self.imagen)
        return '{}{}'.format(STATIC_URL, 'img/empty.png')
    
#     def name_image(self):
#         if self.image:
#             return '{}'.format(self.image)
#         return '{}{}'.format(MEDIA_URL, 'img/empty.png')
#
#     def check_image(self):
#         if self.image:
#             return 1
#         return 0
# """

    def toJSON(self):

        item = model_to_dict(self)
        item['marca'] = self.marca.toJSON()
        item['modelo'] = self.modelo.toJSON()
        item['pvp'] = self.pvp_cal()
        item['imagen'] = self.get_image()
        item['cantidad'] = 1

        return item

    class Meta:
        db_table = 'producto'
        verbose_name = 'producto'
        verbose_name_plural = 'productos'
        ordering = ['-id']

