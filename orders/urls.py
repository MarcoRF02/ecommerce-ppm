from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('order-history/', views.order_history, name='order_history'),
    path('order-success/', views.order_success, name='order_success'),
    path('order-success/<int:order_id>/', views.order_success, name='order_success'),

]