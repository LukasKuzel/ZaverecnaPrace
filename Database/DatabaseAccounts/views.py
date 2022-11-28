from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages

from .models import Profile
from .forms import CreateUserForm



def register_view(request):
    if request.method == 'POST':
        forms = CreateUserForm(request.POST)

        if forms.is_valid():
            user = forms.save()
            userMessage = forms.cleaned_data.get('username')
            #log in the user in
            login(request, user)
            messages.success(request, 'Účet byl vytvořen pro ' + userMessage)
            return redirect('index')
    else:
        forms = CreateUserForm
        #messages.error(request, 'Něco nebyl zadáno správně. Zkuste to prosím znovu.')


    PoslatVen2 = {
        'forms':forms

    }

    return render(request, 'accounts/register.html', context=PoslatVen2)


def login_view(request):
    if request.method == 'POST':
        forms = AuthenticationForm(data=request.POST)
        if forms.is_valid():
            #log in the user
            user = forms.get_user()
            login(request, user)
            return redirect('index')
    else:
        forms = AuthenticationForm()

    PoslatVen3 = {
        'forms': forms

    }

    return render(request, 'accounts/login.html', context=PoslatVen3)


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('index')

