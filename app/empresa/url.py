from django.urls import path
from app.empresa.views import *

app_name = 'empresa'

urlpatterns = [
    path('configuracion/', empresa_create.as_view(), name='configuracion'),

]