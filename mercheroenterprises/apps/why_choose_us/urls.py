from django.urls import path
from . import views

urlpatterns = [
    path('commitment-to-quality', views.why_choose_us_commitment_to_quality, name='why_choose_us_commitment_to_quality'),
    path('advanced-technology', views.why_choose_us_advanced_technology, name='why_choose_us_advanced_technology'),
    path('why-choose-us', views.why_choose_us, name='why_choose_us'),
    path('sustainable-production', views.why_choose_us_sustainable_production, name='why_choose_us_sustainable_production'),
    path('fast-communication-and-support/', views.why_choose_us_fast_communication_and_support, name='why_choose_us_fast_communication_and_support'),
    path('fast-communication-and-support/', views.why_choose_us_fast_communication_and_support, name='why_choose_us_fast_communication_and_support'),
    path('global-delivery-network/', views.why_choose_us_global_deleivery_network, name='why_choose_us_global_deleivery_network'),
    path('skilled-workforce/', views.why_choose_us_skilled_workforce, name='why_choose_us_skilled_workforce'),
    path('oem-expertise/', views.why_choose_us_oem_expertise, name='why_choose_us_oem_expertise'),

]
