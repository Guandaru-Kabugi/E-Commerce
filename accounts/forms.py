from typing import Any
from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
User = get_user_model()

class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['full_name','username','email','phone_number']
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        email = cleaned_data.get('email')
        phone_number = cleaned_data.get('phone_number')

        # Check if username already exists
        if User.objects.filter(username=username).exists():
            raise ValidationError({'username': 'This username is already taken.'})

        # Check if email already exists
        if User.objects.filter(email=email).exists():
            raise ValidationError({'email': 'This email is already registered.'})

        # Check if phone number already exists
        if User.objects.filter(phone_number=phone_number).exists():
            raise ValidationError({'phone_number': 'This phone number is already registered.'})

        return cleaned_data
 
class LoginForm(forms.Form):
    email = forms.EmailField(max_length=200)
    password = forms.CharField(widget=forms.PasswordInput)
