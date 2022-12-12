from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

from .models import Profile
from .forms import CreateUserForm, MyAuthenticationForm
from django.contrib.auth.decorators import login_required


def register_view(request):
    registered = False
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            user_forms = CreateUserForm(request.POST)
            if user_forms.is_valid():
                user = user_forms.save()
                user.save()
                username = user_forms.cleaned_data.get('username')

                if 'image' in request.FILES:
                    user.image = request.FILES['image']
                user.save()
                #log in the user in
                login(request, user)
                messages.success(request, 'Účet byl vytvořen pro ' + username)
                return redirect('index')
                registered = True

            else:
                print(user_forms.errors)
                messages.error(request, 'Něco nebylo zadáno správně. Zkuste to prosím znovu.')
        else:
            user_forms = CreateUserForm




        PoslatVen2 = {
            'user_forms':user_forms,
            'registered':registered

        }

        return render(request, 'accounts/register.html', context=PoslatVen2)


def login_view(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            forms = MyAuthenticationForm(request.POST)
            if forms.is_valid():
                #log in the user
                email = forms.cleaned_data["email"]
                password = forms.cleaned_data["password"]
                user = authenticate(email=email, password=password)
                if user:
                    login(request, user)
                    return redirect('index')
                else:
                    messages.error(request, 'Špatné jméno nebo heslo')
            else:
                messages.error(request, 'Špatné jméno nebo heslo')
        else:
            forms = MyAuthenticationForm()

        PoslatVen3 = {
            'forms': forms,


        }

        return render(request, 'accounts/login.html', context=PoslatVen3)


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('index')

