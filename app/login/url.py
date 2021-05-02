from django.urls import path

from  app.views import connect
from app.login.views import *


urlpatterns = [
    path('', LoginFormView.as_view(), name='login'),
    path('connect/', connect, name='connect'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout')
]
