from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.urls import reverse_lazy
from django.views import generic

from DatabaseApps.models import Review
from .forms import CreateUserForm, MyAuthenticationForm, MyEditForm, MyEditFormPassword, ReviewForm
from .models import Profile

# Funkce pro registraci uživatele
def register_view(request):
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

            else:
                print(user_forms.errors)
        else:
            user_forms = CreateUserForm


        PoslatVen2 = {
            'user_forms':user_forms,

        }

        return render(request, 'accounts/register.html', context=PoslatVen2)

# Funkce pro přihlášení uživatele.
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
                    pass
            else:
                pass
        else:
            forms = MyAuthenticationForm()

        PoslatVen3 = {
            'forms': forms,


        }

        return render(request, 'accounts/login.html', context=PoslatVen3)

# Funkce pro odhlášení
def logout_view(request):
    if request.method == 'POST':
        #Logout user
        logout(request)
        return redirect('index')

#Třída na úpravu údajů
class edit_view(generic.UpdateView):
    form_class = MyEditForm
    template_name = 'accounts/edit.html'
    success_url = reverse_lazy('profile')

    # Vypíše informace o uživateli do daných polí
    def get_object(self, queryset=None):
        return self.request.user

#Třída na změnu hesla
class edit_password_view(generic.UpdateView):
    form_class = MyEditFormPassword
    template_name = 'accounts/password.html'
    success_url = reverse_lazy('login')

    #Vypíše informace o uživateli do daných polí
    def get_object(self, queryset=None):
        return self.request.user

#Třída na vypsání uložených informací daného uživatele
def profile_detail(request):
    profile = Profile.object.filter(id=request.user.id).first()
    review5 = Review.objects.all().filter(user__id=request.user.id)

    PoslatVen = {
        'profile':profile,
        'review5':review5,
    }

    return render(request, 'accounts/profile.html', context=PoslatVen)

#Funkce na odeslání recenze
def submitReview(request, book_id):
    url = request.META.get('HTTP_REFERER')
    if request.user.is_authenticated:
        if request.method == 'POST':
            try:
                reviews = Review.objects.get(user__id=request.user.id, book__id=book_id)
                form_review = ReviewForm(request.POST, instance=reviews)
                form_review.save()
                messages.success(request, 'Vaše recenze byla aktualizována.')
                return redirect(url)
            except:
                form_review = ReviewForm(request.POST)
                if form_review.is_valid():
                    data = Review()
                    data.text = form_review.cleaned_data['text']
                    data.rate = form_review.cleaned_data['rate']
                    data.ip = request.META.get('REMOTE_ADDR')
                    data.book_id = book_id
                    data.user_id = request.user.id
                    data.save()
                    messages.success(request, 'Vaše recenze byla vytvořena.')
                    return redirect(url)

#Funkce na mazání recenze k dané knize
def delete(request, book_id):
  review6 = Review.objects.get(user__id=request.user.id, book__id=book_id)
  review6.delete()
  return redirect('profile')