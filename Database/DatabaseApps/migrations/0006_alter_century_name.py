# Generated by Django 4.1.2 on 2023-01-06 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DatabaseApps', '0005_book_century'),
    ]

    operations = [
        migrations.AlterField(
            model_name='century',
            name='name',
            field=models.CharField(max_length=3, null=True, unique=True),
        ),
    ]
