from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']


    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.email}'


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['city']