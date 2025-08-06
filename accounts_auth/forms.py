from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Layout, Submit




class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'})
    )
    
    username = forms.CharField(
        required=True,
        help_text='Username may only contain alphanumeric characters or single hyphens.',
        widget=forms.TextInput(attrs={'placeholder': 'Choose a username'})
    )
    
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'placeholder': 'Create a password'}),
        error_messages={'required': 'Please enter a password.'}
    )
    
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={'placeholder': 'Repeat your password'}),
        error_messages={'required': 'Please confirm your password.'}
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']




class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
