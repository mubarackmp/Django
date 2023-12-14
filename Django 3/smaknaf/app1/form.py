from django import forms
from .models import *

class userform1(forms.ModelForm):
    class Meta:
        model=users
        fields='__all__'