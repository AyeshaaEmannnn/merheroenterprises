from django.shortcuts import render

# Create your views here.
def why_choose_us_commitment_to_quality(request):
    return render(request, 'why_choose_us/commitmenttoquality.html')

def why_choose_us_advanced_technology(request):
    return render(request, 'why_choose_us/advancedtechnology.html')

def why_choose_us(request):
    return render(request, 'why_choose_us/why_choose_us.html')

def why_choose_us_sustainable_production(request):
    return render(request, 'why_choose_us/sustainableproduction.html')

def why_choose_us_fast_communication_and_support(request):
    return render(request, 'why_choose_us/fastcommunicationandsupport.html')

def why_choose_us_global_deleivery_network(request):
    return render(request, 'why_choose_us/globaldeliverynetwork.html')

def why_choose_us_skilled_workforce(request):
    return render(request, 'why_choose_us/skilledworkforce.html')

def why_choose_us_oem_expertise(request):
    return render(request, 'why_choose_us/oemexpertise.html')