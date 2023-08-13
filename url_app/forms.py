from django import forms
from .models import ShortUrls

class UrlForm(forms.ModelForm):
    class Meta:
        model = ShortUrls
        fields = ['long_url']