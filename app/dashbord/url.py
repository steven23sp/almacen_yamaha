from django.urls import path
from app.dashbord.views import *

app_name = 'dashbord'

urlpatterns = [
    path('', dashbord.as_view(), name='dashbord'),

]
