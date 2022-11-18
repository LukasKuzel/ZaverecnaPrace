from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


def register_view(request):
    if request.method == 'POST':
        forms = UserCreationForm(request.POST)
        if forms.is_valid():
            forms.save()
            #login the user in
            return redirect('index')
    else:
        forms = UserCreationForm

    PoslatVen2 = {
        'forms':forms

    }

    return render(request, 'accounts/register.html', context=PoslatVen2)


def login_view(request):
    if request.method == 'POST':
        forms = AuthenticationForm(data=request.POST)
        if forms.is_valid():
            return redirect('index')
    else:
        forms = AuthenticationForm()

    PoslatVen3 = {
        'forms': forms

    }

    return render(request, 'accounts/login.html', context=PoslatVen3)
