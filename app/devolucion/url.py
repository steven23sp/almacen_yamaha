from django.urls import path
from app.devolucion.views import *

app_name = 'devolucion'

urlpatterns = [

    path('lista/', devolucion_list.as_view(), name='lista'),

]
