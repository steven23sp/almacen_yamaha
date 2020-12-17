from django.urls import path
from app.cargo.views import *

app_name = 'cargo'

urlpatterns = [
    path('lista/', cargo_list.as_view(), name='lista'),
    path('crear/', cargo_create.as_view(), name='crear'),
    path('editar/<int:pk>/', cargo_update.as_view(), name='editar'),
    path('eliminar/<int:pk>/', cargo_delete.as_view(), name='eliminar'),

]
