# Generated by Django 4.1.2 on 2022-12-24 19:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DatabaseApps', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz_question',
            name='delete2',
        ),
        migrations.RemoveField(
            model_name='quiz_question',
            name='quizAnswer',
        ),
        migrations.DeleteModel(
            name='Quiz',
        ),
        migrations.DeleteModel(
            name='Quiz_answer',
        ),
        migrations.DeleteModel(
            name='Quiz_question',
        ),
    ]
