# forms.py
from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['contact_email', 'name', 'contact_number']
        widgets = {
            'contact_email': forms.TextInput(attrs={'placeholder': 'Enter email'}),
            'name': forms.TextInput(attrs={'placeholder': 'Enter name'}),
            'contact_number': forms.TextInput(attrs={'placeholder': 'Enter phone number'}),
        }
