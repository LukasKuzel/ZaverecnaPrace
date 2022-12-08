from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

from .models import Profile
from .forms import CreateUserForm, CreateProfileForm
from django.contrib.auth.decorators import login_required


def register_view(request):
    registered = False
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            user_forms = CreateUserForm(request.POST)
            profile_forms = CreateProfileForm(request.POST)
            if user_forms.is_valid() and profile_forms.is_valid():
                user = user_forms.save()
                user.save()
                username = user_forms.cleaned_data.get('username')

                profile = profile_forms.save(commit=False)
                profile.user = user
                if 'picture' in request.FILES:
                    profile.picture = request.FILES['picture']
                profile.save()
                #log in the user in
                login(request, user)
                messages.success(request, 'Účet byl vytvořen pro ' + username)
                return redirect('index')
                registered = True

            else:
                print(user_forms.errors, profile_forms.errors)
                messages.error(request, 'Něco nebylo zadáno správně. Zkuste to prosím znovu.')
        else:
            user_forms = CreateUserForm
            profile_forms = CreateProfileForm



        PoslatVen2 = {
            'user_forms':user_forms,
            'profile_forms':profile_forms,
            'registered':registered

        }

        return render(request, 'accounts/register.html', context=PoslatVen2)


def login_view(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            forms = AuthenticationForm(data=request.POST)
            if forms.is_valid():
                #log in the user
                user = forms.get_user()
                login(request, user)
                return redirect('index')
            else:
                messages.error(request, 'Špatné jméno nebo heslo')
        else:
            forms = AuthenticationForm()

        PoslatVen3 = {
            'forms': forms,


        }

        return render(request, 'accounts/login.html', context=PoslatVen3)


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('index')

