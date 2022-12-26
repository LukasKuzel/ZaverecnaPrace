from django.contrib.auth.models import User, AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

#Ukládání obrázku do složky image_profile + id uživatele + složka /image/ + název obrázku
def profile_images(instance, filename):
    return "image_profile/" + str(instance.id) + "/image/" + filename

#Třída kountrolující a upravující uživatele a superuživatele
class CustomAccountManager(BaseUserManager):
    def create_superuser(self, email, username, first_name, last_name, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Super uživatel musí mít is_staff=True')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Super uživatel musí mít is_superuser=True')
        return self.create_user(email, username, first_name, last_name, password, **other_fields)

    def create_user(self, email, username, first_name, last_name, password, **other_fields):
        if not email:
            raise ValueError(_('Neplatný email'))
        if not username:
            raise ValueError(_('Neplatné jméno'))

        email = self.normalize_email(email)
        user = self.model(email=email, username=username, first_name=first_name, last_name=last_name,**other_fields)
        user.set_password(password)
        user.save()
        return user

#Třída profil
class Profile(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    age = models.IntegerField(null=True, blank=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9}$')
    phone_number = models.CharField(validators=[phone_regex], max_length=9, blank=True, null=True)
    city = models.CharField(max_length=250, blank=True, null=True)
    street = models.CharField(max_length=250, blank=True, null=True)
    PCS_regex = RegexValidator(regex=r'^\+?1?\d{5}$')
    PCS = models.CharField(validators=[PCS_regex],max_length=5, blank=True, null=True)
    image = models.ImageField(upload_to=profile_images, blank=True, null=True)
    about = models.TextField(_('about'), max_length=1000, blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    object = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name','last_name']

    def __str__(self):
        return self.username

