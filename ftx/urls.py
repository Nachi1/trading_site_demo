from django.urls import path
from . import views

app_name= 'ftx'

urlpatterns = [
    path('', views.home, name= 'home'),
    path('dashboard/', views.dashboard, name= 'dashboard'),
    path('transaction_history/', views.transaction_history, name= 'transaction_history'),
    # path('get_data', views.get_data, name='get_data'),
    path('stock/', views.stock, name='stock'),
]