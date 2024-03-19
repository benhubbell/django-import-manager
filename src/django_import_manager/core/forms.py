from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.models import User
class SignupForm(forms.Form):
    username = forms.CharField()
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())
    token = forms.CharField()

    # def clean(self):
    #     cleaned_data = super().clean()

    #     password = cleaned_data.get('password')
    #     confirm_password = cleaned_data.get('confirm-password')
    #     print("ahahahahahahahahahaha")
    #     print(cleaned_data)
    #     if password != confirm_password:
    #         raise ValidationError({'password': ["Passwords do not match",]})

    #     return cleaned_data
    
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 != password2:
            raise ValidationError({'password1': ["Passwords do not match",]})

        return cleaned_data

