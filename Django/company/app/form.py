from django import forms
from app.models import *


class Employeform(forms.ModelForm):
    class Meta:
        model=Employee
        fields='__all__'
        
class Employform(forms.ModelForm):
    class Meta:
        model=Employ
        fields='__all__'


