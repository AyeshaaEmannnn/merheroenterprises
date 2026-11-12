from django.shortcuts import render

# Create your views here.
def cataloge(request):
    return render(request, 'cataloge/cataloge.html')