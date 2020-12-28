from django.urls import path
from app.empresa.views import *

app_name = 'empresa'

urlpatterns = [
    path('lista/', empresa_list.as_view(), name='lista'),
    #path('crear/', cliente_create.as_view(), name='crear'),
    path('editar/<int:pk>/', empresa_update.as_view(), name='editar'),
    path('eliminar/<int:pk>/', empresa_delete.as_view(), name='eliminar'),

]
