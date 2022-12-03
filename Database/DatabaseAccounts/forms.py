from django.contrib.auth import password_validation
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile, User


class CreateUserForm(UserCreationForm):
    username = forms.CharField(required=True, error_messages={'required': 'Zadejte prosím své přihlašovací jméno.'})
    first_name = forms.CharField(required=True, error_messages={'required': 'Zadejte prosím své křestní jméno.'})
    last_name = forms.CharField(required=True, error_messages={'required': 'Zadejte prosím své přijímení.'})
    email = forms.EmailField(required=True, error_messages={'required': 'Zadejte prosím nepoužitý email.'})

    class Meta:
        model = User
        model._meta.get_field('email')._unique = True
        fields = ['username','first_name','last_name','email','password1','password2']

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.email}'


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['city']