# views.py
from django.shortcuts import render

def about_introduction(request):
    return render(request, 'about/introduction.html')

def about_our_journey(request):
    return render(request, 'about/our_journey.html')

def about_vision(request):
    return render(request, 'about/vision.html')

# aur baki pages bhi isi tarah
def about_team(request):
    return render(request, 'about/team.html')

def about_certificates(request):
    return render(request, 'about/certificates.html')   

def about_core_values(request):
    return render(request, 'about/core_values.html')
def about_company_profile(request):
    return render(request, 'about/company_profile.html')