from django import forms
from .models import Shortener

class ShortenerForm(forms.ModelForm):
    long_url = forms.URLField()

    class Meta:
        model = Shortener
        fields = ['long_url']