from django import forms
from .models import PurchaseOrder
from profiles.models import UserProfile


class PurchaseOrderForm(forms.ModelForm):
    class Meta:
        model = PurchaseOrder
        fields = ("first_name", "last_name", "email")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            "first_name": "First Name*",
            "last_name": "Last Name*",
            "email": "Email Address*"
        }
        self.fields['first_name'].widget.attrs['autofocus'] = True
        
        self.fields['last_name'].widget.attrs['value'] = UserProfile.last_name
        self.fields['email'].widget.attrs['value'] = UserProfile.email
        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = True
            self.fields[field].widget.attrs['class'] = 'formstyle'
