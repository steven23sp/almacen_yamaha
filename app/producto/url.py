from django.urls import path
from app.producto.views import *

app_name = 'producto'

urlpatterns = [
    path('lista/', producto_list.as_view(), name='lista'),
    path('crear/', producto_create.as_view(), name='crear'),
    path('editar/<int:pk>/', producto_update.as_view(), name='editar'),
    path('eliminar/<int:pk>/', producto_delete.as_view(), name='eliminar')

]
