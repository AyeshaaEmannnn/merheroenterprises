from django.shortcuts import render

# Create your views here.
def leathercollection(request):
    return render(request, 'leathercollection/leathercollection.html')