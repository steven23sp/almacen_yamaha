from django.contrib.auth.decorators import login_required
from django.urls import path
from app.venta.views import *

app_name = 'venta'

urlpatterns = [
    path('crear/', venta_create.as_view(), name='crear'),
    path('lista/', venta_list.as_view(), name='lista'),
    path('printpdf/<int:pk>', login_required(printpdf.as_view()), name='printpdf'),
    path('reporte_total', venta_report_total.as_view(), name='reporte_total'),
    # path('editar/<int:pk>/', cargo_update.as_view(), name='editar'),
    # path('eliminar/<int:pk>/', cargo_delete.as_view(), name='eliminar'),

]
