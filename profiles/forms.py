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
            'first_name': 'First Name',
            'last_name': 'Last Name',
        }
        self.fields['first_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'formstyle'
