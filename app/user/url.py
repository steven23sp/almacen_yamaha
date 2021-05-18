from django.urls import path
from app.user.views import *


app_name = 'user'

urlpatterns = [
    path('lista/', user_list.as_view(), name='lista'),
    path('crear/', user_create.as_view(), name='crear'),
    path('editar/<int:pk>/', user_update.as_view(), name='editar'),
    path('groups/', list_group.as_view(), name='lista_grupo'),
    path('group_crear/', create_group.as_view(), name='crear_grupo'),
    path('group_editar/<int:pk>/', update_group.as_view(), name='editar_grupo'),

]
