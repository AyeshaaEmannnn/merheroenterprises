# from django.urls import path
# from . import views
# [
# path('inquiry/', views.contact_inquiry_form, name='contact_inquiry_form'),
# path('details/', views.contact_contact_details, name='contact_contact_details'),
# path('map/', views.contact_google_map, name='contact_google_map'),
# path('faqs/', views.contact_faqs, name='contact_faqs'),
# ]
# urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path("inquiry-form/", inquiry_view, name="contact_inquiry_form"),
    path('contact-details/', contact_contact_details, name='contact_contact_details'),
    path('map/', contact_google_map, name='contact_google_map'),
    path('faqs/', contact_faqs, name='contact_faqs'),
]