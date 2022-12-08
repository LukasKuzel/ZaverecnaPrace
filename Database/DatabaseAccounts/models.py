from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User, AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


def profile_images(instance, filename):
    return "image_profile/" + str(instance.id) + "/image/" + filename

class Profile(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    age = models.IntegerField(null=True, blank=True)
    phone_number = models.CharField(max_length=12,null=True, blank=True)
    city = models.CharField(max_length=250, null=True, blank=True)
    street = models.CharField(max_length=250, null=True, blank=True)
    PCS = models.CharField(max_length=250, null=True, blank=True)
    image = models.ImageField(upload_to=profile_images, blank=True)
    timestamp = models.DateTimeField

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

#Úprava ADMIN panelu
#class CustomUserAdmin(UserAdmin):
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    #add_fieldsets = (
        #(None, {
            #'classes': ('wide',),
            #'fields': ('username', 'email', 'password1', 'password2'),
        #}),
    #)