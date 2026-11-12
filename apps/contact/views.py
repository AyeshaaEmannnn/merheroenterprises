# from django.shortcuts import render

# # Create your views here.
# def contact_inquiry_form(request):
#     return render(request, 'contact/inquiry_form.html')

# def contact_contact_details(request):
#     return render(request, 'contact/contact_details.html')

# def contact_google_map(request):
#     return render(request, 'contact/google_map.html')

# def contact_faqs(request):
#     return render(request, 'contact/faqs.html')
# views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import InquiryForm

def inquiry_view(request):

    if request.method == "POST":

        form = InquiryForm({
            "full_name": request.POST.get("name"),
            "email": request.POST.get("email"),
            "phone": request.POST.get("phone"),
            "subject": request.POST.get("subject"),
            "message": request.POST.get("message"),
        })

        if form.is_valid():
            form.save()
            messages.success(request, "Your inquiry has been sent successfully.")
            return redirect("contact")   # change according to your url name

        else:
            messages.error(request, "Please correct the errors below.")

    else:
        form = InquiryForm()

    return render(request, "contact/inquiryform.html", {"form": form})

def contact_contact_details(request):
    return render(request, 'contact/contact_details.html')

def contact_google_map(request):
    return render(request, 'contact/map.html')

def contact_faqs(request):
    return render(request, 'contact/faq.html')