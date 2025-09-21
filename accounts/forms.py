from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model


class RegisterForm(forms.Form):
    username = forms.CharField(label="Username", max_length=30, validators=[MinLengthValidator(2)])
    fullname = forms.CharField(label="Full Name", max_length=30, validators=[MinLengthValidator(3)])
    address = forms.CharField(label="Address", max_length=50, validators=[MinLengthValidator(7)])
    phone_number = forms.IntegerField(label="Phone Number")
    password = forms.CharField(label="Password", widget=forms.PasswordInput, validators=[MinLengthValidator(6)])
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput, validators=[MinLengthValidator(6)])
    
    def clean_password(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        
        if password and password2 and password != password:
            raise ValidationError("Password don't match.")
        
        return password2

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder': 'Username'})
        self.fields['password'].widget.attrs.update({'placeholder': 'Password'})
        