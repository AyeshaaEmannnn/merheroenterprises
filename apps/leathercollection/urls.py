from django.urls import path
from . import views

urlpatterns = [
    path('leathercollection/', views.leathercollection, name='leathercollection'),

]
