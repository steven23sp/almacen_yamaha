from django.contrib import admin
from .models import *

class VentaAdmin(admin.TabularInline):
    model = detalle_venta


class Detalle_ventaAdmin(admin.ModelAdmin):
    inlines = (VentaAdmin, )


admin.site.register(venta, Detalle_ventaAdmin)
