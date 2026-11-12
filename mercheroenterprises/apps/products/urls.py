from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.products_list, name='products_list'),
    path('products/item/<slug:product_slug>/', views.product_detail, name='product_detail'),
    path('products/category/<slug:category_slug>/', views.category_detail, name='category_detail'),
    path('products/category/<slug:category_slug>/<slug:subcategory_slug>/', views.subcategory_detail, name='subcategory_detail'),
]
