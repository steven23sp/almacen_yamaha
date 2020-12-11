from django.urls import path
from app.proveedor.views import *

app_name = 'proveedor'

urlpatterns = [
    path('lista/', proveedor_list.as_view(), name='lista'),
    path('crear/', proveedor_create.as_view(), name='crear'),
    path('editar/<int:pk>/', proveedor_update.as_view(), name='editar'),
    path('eliminar/<int:pk>/', proveedor_delete.as_view(), name='eliminar'),

]
