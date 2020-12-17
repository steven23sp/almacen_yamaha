from django.urls import path
from app.empleado.views import *

app_name = 'empleado'

urlpatterns = [
    path('lista/', empleado_list.as_view(), name='lista'),
    path('crear/', empleado_create.as_view(), name='crear'),
    path('editar/<int:pk>/', empleado_update.as_view(), name='editar'),
    path('eliminar/<int:pk>/', empleado_delete.as_view(), name='eliminar'),

]
