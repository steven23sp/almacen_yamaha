from django.urls import path
from app.marca.views import *

app_name = 'marca'

urlpatterns = [
    path('lista/', marca_list.as_view(), name='lista'),
    path('crear/', marca_create.as_view(), name='crear'),
    path('editar/<int:pk>/', marca_update.as_view(), name='editar'),
    path('eliminar/<int:pk>/', marca_delete.as_view(), name='eliminar'),

]
