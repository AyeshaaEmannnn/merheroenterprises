# forms.py
from django import forms
from .models import Inquiry

class InquiryForm(forms.ModelForm):

    class Meta:
        model = Inquiry
        fields = ['full_name', 'email', 'phone', 'subject', 'message']

    def clean_phone(self):
        phone = self.cleaned_data.get("phone")
        if phone and not phone.replace("+", "").replace(" ", "").isdigit():
            raise forms.ValidationError("Invalid phone number format.")
        return phone