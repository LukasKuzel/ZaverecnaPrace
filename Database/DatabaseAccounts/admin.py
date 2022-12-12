from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Profile

# Register your models here.
class UserAdminConfig(UserAdmin):
    search_fields = ('email','username','last_name',)
    list_filter = ('email','username','last_name','is_active','is_staff')
    ordering = ('-username',)
    list_display = ('username','email','last_name','is_active','is_staff')

    fieldsets = (
        (None, {'fields':('email','username','first_name','last_name',)}),
        ('Personal', {'fields':('age','phone_number','city','street','PCS','image','about',)}),
        ('Permission', {'fields': ('is_staff', 'is_active','is_superuser')}),
    )
    add_fieldsets = (
        (None, {
        'classes':('wide',),
        'fields':('email','username','first_name','last_name','password1','password2','is_staff','is_active','is_superuser')}
        ),
    )


admin.site.register(Profile, UserAdminConfig)
