from django.contrib import admin
from .models import *

admin.site.register(Nation)
admin.site.register(Genre)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Review)
admin.site.register(Quiz_answer)
admin.site.register(Quiz_question)
admin.site.register(Quiz)

