from django.urls import path

from . import views

app_name = 'store'

urlpatterns = [
    path('', views.all_products, name='all_products'),
    path('item/<slug:slug>/',views.product_detail,name='product_detail'), #primo slug si riferisce al tipo di dato e il secondo all'item
    path('search/<slug:category_slug>/',views.category_list, name='category_list'),
    path('home/', views.all_products, name='home'), #new
    path('search/', views.search, name='search'),
]