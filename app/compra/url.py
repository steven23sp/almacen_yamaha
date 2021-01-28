from django.urls import path
from app.compra.views import *

app_name = 'compra'

urlpatterns = [
    path('crear/', compra_create.as_view(), name='crear'),
    path('lista/', compra_list.as_view(), name='lista'),
    path('factura/<int:pk>/', pdfcompra.as_view(), name='factura'),
    #path('eliminar/<int:pk>/', cargo_delete.as_view(), name='eliminar'),

]
