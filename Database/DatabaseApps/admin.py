from django.contrib import admin
from .models import *


admin.site.register(Genre)

class FilterA(admin.ModelAdmin):
    search_fields = ('name','surname')
    list_filter = ('name','surname')

admin.site.register(Author, FilterA)

class FilterB(admin.ModelAdmin):
    search_fields = ('name','name')
    list_filter = ('name','name')

admin.site.register(Book,FilterB)


class CommentAdmin(admin.ModelAdmin):
    list_filter = ('user', 'book',)
    list_display = ('user','book','text','rate','created_date','updated_date','status')
    ordering = ('-user',)

admin.site.register(Review, CommentAdmin)


class FilerN(admin.ModelAdmin):
    search_fields = ('state','state')
    list_filter = ('state','state')

admin.site.register(Nation, FilerN)

admin.site.register(Century)