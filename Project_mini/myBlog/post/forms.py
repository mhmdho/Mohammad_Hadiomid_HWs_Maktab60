from django import forms
from .models import  Tag,Category,Post
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError



class LoginForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput)