from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


def poster_book_path(instance, filename):
    return "book/" + str(instance.id) + "/book_poster/" + filename


def poster_author_path(instance, filename):
    return "author/" + str(instance.id) + "/author_poster/" + filename

#Kvůli času narychlo udělaná třída. Ještě budu upravovat + to birthdate a death date
class Nation(models.Model):
    state = models.CharField(max_length=250, verbose_name="State")
    city = models.CharField(max_length=250, verbose_name="City")


class Genre(models.Model):
    name = models.CharField(max_length=60, unique=True)

    def __str__(self):
        return self.name


class Quiz_answer(models.Model):
    answer = models.CharField(max_length=250, verbose_name="Answer")
    verify = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(1)], null=False, verbose_name="0-false or 1-true")


class Quiz_question(models.Model):
    question = models.CharField(max_length=250, verbose_name="Question")
    quizAnswer = models.ManyToManyField(Quiz_answer)
    delete2 = models.ForeignKey(Quiz_answer, on_delete=models.CASCADE, related_name='delete_answers')


class Quiz(models.Model):
    quizQuestion = models.ManyToManyField(Quiz_question)
    delete1 = models.ForeignKey(Quiz_question, on_delete=models.CASCADE, related_name='delete_question')


class Author(models.Model):
    name = models.CharField(max_length=250, unique=False, verbose_name="Name")
    surname = models.CharField(max_length=250, unique=False, verbose_name="Surname")
    nation = models.ManyToManyField(Nation)
    birthdate = models.CharField(max_length=100, verbose_name="birthdate", null=True)
    deathdate = models.CharField(max_length=100, verbose_name="death date", null=True)
    photo = models.ImageField(upload_to=poster_author_path, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    nation = models.ManyToManyField(Nation)


    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f'{self.name} {self.surname}'


class Book(models.Model):
    name = models.CharField(max_length=250, verbose_name="Title")
    rate = models.FloatField(default=0, validators=[MinValueValidator(1), MaxValueValidator(100)], blank=True,
                             null=True, help_text="Enter between 1 - 100")
    photo = models.ImageField(upload_to=poster_book_path, blank=True, null=True)
    plot = models.TextField(blank=True, null=True)
    genre = models.ManyToManyField(Genre)
    author = models.ManyToManyField(Author)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f'{self.name}'


class Review(models.Model):
    text = models.TextField
    rate = models.FloatField(default=0, validators=[MinValueValidator(1), MaxValueValidator(5)], blank=True,
                             null=True, help_text="Enter between 1 - 5")
    book = models.ManyToManyField(Book)

    def __str__(self):
        return self.text




