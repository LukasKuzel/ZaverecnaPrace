from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.utils.translation import gettext_lazy as _
from django import forms

from DatabaseApps.models import Review
from .models import Profile


class CreateUserForm(UserCreationForm):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    city = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    street = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    PCS = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    phone_number = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    age = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    about = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Profile
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.email}'

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if Profile.object.filter(username=username).exists():
            raise forms.ValidationError(_("Tato přezdívka se již používá."))
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Profile.object.filter(email=email).exists():
            raise forms.ValidationError(_("Tento email se již používá."))
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(_("Hesla se neshodují"))
        return password2


class MyAuthenticationForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"autofocus": True, 'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        user = authenticate(email=email, password=password)
        if not user:
            raise forms.ValidationError(_("Špatný email nebo heslo."))



class MyEditForm(UserChangeForm):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}), disabled=True)
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    city = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    street = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    PCS = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={'class': 'form-control', 'type':'number', 'min':'0'}))
    phone_number = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={'class': 'form-control', 'type':'number', 'min':'0'}))
    age = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={'class': 'form-control', 'type':'number', 'min':'0'}))
    about = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Profile
        fields = ['image','username','first_name','last_name','email','city','street','PCS','age','phone_number','about']


class MyEditFormPassword(UserCreationForm):
    password1 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Profile
        fields = ['password1','password2']

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(_("Hesla se neshodují"))
        return password2

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text','rate']
