from django import forms
from .models import UserProfile


class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'personal_info_first_name': 'First Name',
            'personal_info_last_name': 'Last Name',
            'default_billing_address_line1': 'Street Address 1',
            'default_billing_address_line2': 'Street Address 2',
            'default_billing_address_postcode': 'Postcode or ZIP',
            'default_billing_address_country': 'Country',
        }

        self.fields['personal_info_first_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = ''
            self.fields[field].label = False
