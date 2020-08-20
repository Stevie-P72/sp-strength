from django import forms
from .models import UserProfile


class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'email': 'email',
            'personal_info_first_name': 'First Name',
            'personal_info_last_name': 'Last Name',
        }
        self.fields['personal_info_first_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'formstyle'

