from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.ModelForm):
    class Meta:
        model=Doctor
        fields='__all__'