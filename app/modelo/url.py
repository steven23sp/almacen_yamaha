from django.urls import path
from app.modelo.views import *

app_name = 'modelo'

urlpatterns = [
    path('lista/', modelo_list.as_view(), name='lista'),
    path('crear/', modelo_create.as_view(), name='crear'),
    path('editar/<int:pk>/', modelo_update.as_view(), name='editar'),
    path('eliminar/<int:pk>/', modelo_delete.as_view(), name='eliminar'),

]
