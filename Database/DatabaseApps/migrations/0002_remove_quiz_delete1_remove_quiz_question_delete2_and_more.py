# Generated by Django 4.1.2 on 2022-10-27 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DatabaseApps', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='delete1',
        ),
        migrations.RemoveField(
            model_name='quiz_question',
            name='delete2',
        ),
        migrations.AlterField(
            model_name='review',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]