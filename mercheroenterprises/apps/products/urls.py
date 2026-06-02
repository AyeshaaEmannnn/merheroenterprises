from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.products_list, name='products_list'),
    path('products/motorcycle-racing-suit/', views.motorcycle_racing_suit, name='motorcycle_racing_suit'),
]

