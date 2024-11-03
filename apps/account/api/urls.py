from django.urls import path,include
from .views import *



urlpatterns = [
    path('users-login/', UsersLoginView.as_view(), name='admin_login'),
]