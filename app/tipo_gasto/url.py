from django.urls import path
from app.tipo_gasto.views import *

app_name = 'tipo_gasto'

urlpatterns = [
    path('lista/', tgasto_list.as_view(), name='lista'),
    path('crear/', tgasto_create.as_view(), name='crear'),
    path('editar/<int:pk>/', tgasto_update.as_view(), name='editar'),
    #path('eliminar/<int:pk>/', tgasto_delete.as_view(), name='eliminar'),

]
