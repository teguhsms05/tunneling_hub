



from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control",
                
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))


class SignUpForm(UserCreationForm):
    # first_name = forms.CharField(max_length=101, 
    #     widget=forms.TextInput(
    #         attrs={
    #             "placeholder": "Firstname",
    #             "class": "form-control"
    #         }
    #     ))
    # last_name = forms.CharField(max_length=101, 
    #     widget=forms.TextInput(
    #         attrs={
    #             "placeholder": "Lastname",
    #             "class": "form-control"
    #         }
    #     ))
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control",
                "data-v-min-length": "5"
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control"
            }
        ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control",
                "title": "password",
                "id": "password",
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password check",
                "class": "form-control",
                "data-v-equal": "#password"
            }
        ))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
