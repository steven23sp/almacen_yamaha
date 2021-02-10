from django.urls import path
from app.user.views import *

app_name = 'user'

urlpatterns = [
    path('lista/', user_list.as_view(), name='lista'),
    path('crear/', user_create.as_view(), name='crear'),
    path('editar/<int:pk>/', user_update.as_view(), name='editar'),
    #path('eliminar/<int:pk>/', user_delete.as_view(), name='eliminar'),

]
