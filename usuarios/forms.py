from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Digite sua nome de usuario',
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Digite seu email',
                },
            ),
        }

    password1 = forms.CharField(
        label='Password', 
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite sua senha',
            })
    )
    password2 = forms.CharField(
        label='Confirm Password', 
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Confirme sua senha',
            })
    )

class LoginForm(forms.Form):
    username = forms.CharField(
        label='Username', 
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Informe seu nome de usuario',
            })
    )
    password = forms.CharField(
        label='Password', 
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Informe sua senha',
            }
        )
    )
