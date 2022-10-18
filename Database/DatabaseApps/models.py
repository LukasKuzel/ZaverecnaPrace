from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=60, unique=True)

    def __str__(self):
        return self.name


class Profile(models.Model):
    name = models.CharField(max_length=250, unique=True)
    surname = models.CharField(max_length=250, unique=True)
    birthdate = models.DateField
    email = models.CharField(max_length=250, null=False)
    phone_number = models.IntegerField(null=False)
    password = models.CharField(max_length=250, unique=True, null=False)
    city = models.CharField(max_length=250, null=False)
    street = models.CharField(max_length=250, null=False)
    PCS = models.CharField(max_length=250, null=True)
    timestamp = models.DateTimeField

    def __str__(self):
        return self.name


class Quiz_answer(models.Model):
    answer = models.CharField(max_length=250, verbose_name="Answer")
    verify = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(1)], null=False, verbose_name="0-false or 1-true")


class Quiz_question(models.Model):
    question = models.CharField(max_length=250, verbose_name="Question")
    quizAnswer = models.ManyToManyField(Quiz_answer)


class Quiz(models.Model):
    quizQuestion = models.ManyToManyField(Quiz_question)



class Author(models.Model):
    name = models.CharField(max_length=250, unique=True, verbose_name="Name")
    surname = models.CharField(max_length=250, unique=True, verbose_name="Surname")
    birthdate = models.DateField
    photo = models.ImageField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=250, unique=True, verbose_name="Title")
    rate = models.FloatField(default=0, validators=[MinValueValidator(1), MaxValueValidator(100)], blank=True,
                             null=True, help_text="Enter between 1 - 100")
    photo = models.ImageField(blank=True, null=True)
    plot = models.TextField(blank=True, null=True)
    genre = models.ManyToManyField(Genre)
    author = models.ManyToManyField(Author)

    def __str__(self):
        return self.name


class Review(models.Model):
    text = models.TextField
    rate = models.FloatField(default=0, validators=[MinValueValidator(1), MaxValueValidator(5)], blank=True,
                             null=True, help_text="Enter between 1 - 5")
    profile = models.ManyToManyField(Profile)
    book = models.ManyToManyField(Book)

    def __str__(self):
        return self.text



