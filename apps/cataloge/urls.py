from django.urls import path
from .views import *

urlpatterns = [
    path("cataloge/", cataloge, name="cataloge"),
]