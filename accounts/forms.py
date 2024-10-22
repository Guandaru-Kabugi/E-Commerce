from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
User = get_user_model()

class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['full_name','username','email','phone_number']
class LoginForm(forms.Form):
    email = forms.EmailField(max_length=200)
    password = forms.CharField(widget=forms.PasswordInput)