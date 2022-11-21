from django.db import models


class Profile(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=250)
    surname = models.CharField(max_length=250)
    birthdate = models.DateField
    email = models.CharField(max_length=250, null=False, unique=True)
    phone_number = models.IntegerField(null=False)
    password = models.CharField(max_length=250, null=False)
    city = models.CharField(max_length=250, null=False)
    street = models.CharField(max_length=250, null=False)
    PCS = models.CharField(max_length=250, null=True)
    timestamp = models.DateTimeField

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.name} {self.surname} {self.email}'
