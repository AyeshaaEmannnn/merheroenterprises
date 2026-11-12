from django.shortcuts import render

def team_leader_ceo_message(request):
    return render(request, 'team/leader_ceo_message.html')

def team_director_and_managment_team(request):
    return render(request, 'team/director_and_managment_team.html')

def team_production_and_design_team(request):
    return render(request, 'team/production_and_design_team.html')