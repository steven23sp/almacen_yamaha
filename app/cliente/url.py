from django.urls import path
from app.cliente.views import *

app_name = 'cliente'

urlpatterns = [
    path('lista/', cliente_list.as_view(), name='lista'),
    path('crear/', cliente_create.as_view(), name='crear'),
    path('editar/<int:pk>/', cliente_update.as_view(), name='editar'),
    path('eliminar/<int:pk>/', cliente_delete.as_view(), name='eliminar'),
    path('reporte/', report.as_view(), name='reporte'),

]
