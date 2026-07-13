from django.urls import path
from . import views

urlpatterns = [
    path('introduction/', views.about_introduction, name='about_introduction'),
    path('our-journey/', views.about_our_journey, name='about_our_journey'),
    path('vision/', views.about_vision, name='about_vision'),
    path('team/', views.about_team, name='about_team'),
    path('certificates/', views.about_certificates, name='about_certificates'),
    path('core-values/', views.about_core_values, name='about_core_values'),
    path('company-profile/', views.about_company_profile, name='about_company_profile'),
]
