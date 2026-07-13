from django.shortcuts import render

def capabilities(request):
    return render(request, 'capabilities/capabilities.html')

def capabilities_manufacturing_facility(request):
    return render(request, 'capabilities/manufacturing_facility.html')

def capabilities_research_and_development(request):
    return render(request, 'capabilities/research_and_development.html')

def capabilities_quality_assurance(request):
    return render(request, 'capabilities/quality_assurance.html')

def capabilities_oem_and_customization(request):
    return render(request, 'capabilities/oem_and_customization.html')

def capabilities_work_process(request):
    return render(request, 'capabilities/work_process.html')

def capabilities_sustainability(request):
    return render(request, 'capabilities/sustainability.html')

def capabilities_collaborate_with_us(request):
    return render(request, 'capabilities/collaborate_with_us.html')
