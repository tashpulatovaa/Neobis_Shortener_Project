from django import forms
from .models import ShortUrls

class Urlform(forms.ModelForm):
    class Meta:
        model = ShortUrls
        fields = ['long_url']