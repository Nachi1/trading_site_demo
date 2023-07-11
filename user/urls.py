from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import Register_

app_name= 'user'

urlpatterns = [
    path('register/', Register_.as_view(), name='register'),
    path('login/', views.login_, name='login')
]