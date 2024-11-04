from django.urls import path,include
from .views import *



urlpatterns = [
    path('users-login/', UsersLoginView.as_view(), name='admin_login'),
    path('users-register/', RegisterView.as_view(), name='users-register')
]