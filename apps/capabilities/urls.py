from django.urls import path
from . import views

urlpatterns = [
    path('capabilities/', views.capabilities, name='capabilities'),

    path('manufacturing-facility/', views.capabilities_manufacturing_facility, name='capabilities_manufacturing_facility'),

    path('research-development/', views.capabilities_research_and_development, name='research_and_development'),

    path('quality-assurance/', views.capabilities_quality_assurance, name='quality_assurance'),

    path('oem-customization/', views.capabilities_oem_and_customization, name='oem_and_customization'),

    path('work-process/', views.capabilities_work_process, name='work_process'),

    path('sustainability/', views.capabilities_sustainability, name='sustainability'),

    path('collaborate-with-us/', views.capabilities_collaborate_with_us, name='collaborate_with_us'),
]
