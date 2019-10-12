from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserInfo

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'autofocus': True}),
            'email': forms.EmailInput(attrs={'class': 'input', 'required': True}),
        }



# class LoginForm(AuthenticationForm):
#     username = UsernameField(
#         widget=forms.TextInput(attrs={'class': 'input', 'autofocus': True, 'placeholder': 'username'})
#     )
#     password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'password'}))
