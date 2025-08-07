from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('task/', views.task_dashboard, name='task_dashboard'),
    path('product/', views.product_list, name='product_list'),
    path('transaction/', views.transaction_list, name='transaction_list'),
    path('stock/', views.stock_report, name='stock_report'),
]
