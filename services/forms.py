from django import forms
from .views import Training_Type


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Training_Type
        fields = ['description', 'article', 'image', 'price']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'description': 'description',
            'article': 'article content',
            'image': 'image',
            'price': 'price',
        }
        self.fields['description'].widget.attrs['autofocus'] = True
        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = ''
            self.fields[field].label = False
