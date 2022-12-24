from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from DatabaseAccounts.models import Profile


def poster_book_path(instance, filename):
    return "book/" + str(instance.id) + "/book_poster/" + filename


def poster_author_path(instance, filename):
    return "author/" + str(instance.id) + "/author_poster/" + filename

#Kvůli času narychlo udělaná třída. Ještě budu upravovat + to birthdate a death date
class Nation(models.Model):
    state = models.CharField(max_length=250, verbose_name="State", blank=True)
    city = models.CharField(max_length=250, verbose_name="City", blank=True)

    def __str__(self):
        return f'{self.state} - {self.city}'

class Genre(models.Model):
    name = models.CharField(max_length=60, unique=True)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=250, unique=False, verbose_name="Name", blank=False)
    surname = models.CharField(max_length=250, unique=False, verbose_name="Surname", blank=False)
    nation = models.ManyToManyField(Nation)
    birthdate = models.CharField(max_length=100, verbose_name="birthdate", null=True, blank=True)
    deathdate = models.CharField(max_length=100, verbose_name="death date", null=True, blank=True)
    photo = models.ImageField(upload_to=poster_author_path, blank=False, null=True)
    bio = models.TextField(blank=False, null=True)
    nation = models.ManyToManyField(Nation)


    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f'{self.name} {self.surname}'


class Book(models.Model):
    name = models.CharField(max_length=250, verbose_name="Title", blank=False)
    rate = models.FloatField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)], blank=False,
                             null=True, help_text="Enter between 1 - 5")
    photo = models.ImageField(upload_to=poster_book_path, blank=False, null=True)
    plot = models.TextField(blank=False, null=True)
    genre = models.ManyToManyField(Genre)
    author = models.ManyToManyField(Author)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f'{self.name}'


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    text = models.TextField(blank=True)
    rate = models.FloatField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)], blank=True,
                             null=True, help_text="Enter between 1 - 5")
    status = models.BooleanField(default=True)
    ip = models.CharField(max_length=40,null=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    updated_date = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return str(self.user)




