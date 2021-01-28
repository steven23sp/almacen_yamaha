from django.urls import path
from app.gasto.views import *

app_name = 'gasto'

urlpatterns = [
    path('lista/', gasto_list.as_view(), name='lista'),
    path('crear/', gasto_create.as_view(), name='crear'),
    path('editar/<int:pk>/', gasto_update.as_view(), name='editar'),
    #path('eliminar/<int:pk>/', gasto_delete.as_view(), name='eliminar'),

]
