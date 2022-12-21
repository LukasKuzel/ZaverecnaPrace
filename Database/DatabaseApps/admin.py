from django.contrib import admin
from .models import *

admin.site.register(Nation)
admin.site.register(Genre)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Quiz_answer)
admin.site.register(Quiz_question)
admin.site.register(Quiz)


class CommentAdmin(admin.ModelAdmin):
    list_filter = ('user', 'book',)
    list_display = ('user','book','text','rate','created_date','updated_date','status')
    ordering = ('-user',)

admin.site.register(Review, CommentAdmin)

