from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm

from users.models import User


class UserRegistrationForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'register__fields__email', 'placeholder': 'Email'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'register__fields__username', 'placeholder': 'Username'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'register__fields__firstname', 'placeholder': 'First name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'register__fields__lastname', 'placeholder': 'Last name'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'register__fields__password', 'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'register__fields__repairpassword', 'placeholder': 'Repair password'}))

    class Meta:
        model = User
        fields = ('email', 'username', 'first_name', 'last_name', 'password1', 'password2', )


class UserLoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'login__fields__username', 'placeholder': 'Username'
        }))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'login__fields__password', 'placeholder': 'Password'
        }))

    class Meta:
        model = User
        fields = ('username', 'password', )
