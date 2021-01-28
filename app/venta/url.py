from django.urls import path
from app.venta.views import *

app_name = 'venta'

urlpatterns = [
    path('crear/', venta_create.as_view(), name='crear'),
    path('lista/', venta_list.as_view(), name='lista'),
    # path('editar/<int:pk>/', cargo_update.as_view(), name='editar'),
    # path('eliminar/<int:pk>/', cargo_delete.as_view(), name='eliminar'),

]
