from django.urls import path
from . import views

urlpatterns = [
    path('Founder-Ceo-Message', views.team_leader_ceo_message, name='team_leader_ceo_message'),
    path('director-and-managment-team',views.team_director_and_managment_team, name='team_director_and_managment_team'),
    path('production-and-design-team',views.team_production_and_design_team, name='team_production_and_design_team'),
]
