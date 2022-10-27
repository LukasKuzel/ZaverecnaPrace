# Generated by Django 4.1.2 on 2022-10-27 14:47

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250, unique=True, verbose_name='Name')),
                ('surname', models.CharField(max_length=250, unique=True, verbose_name='Surname')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='')),
                ('bio', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250, unique=True, verbose_name='Title')),
                ('rate', models.FloatField(blank=True, default=0, help_text='Enter between 1 - 100', null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)])),
                ('photo', models.ImageField(blank=True, null=True, upload_to='')),
                ('plot', models.TextField(blank=True, null=True)),
                ('author', models.ManyToManyField(to='DatabaseApps.author')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250, unique=True)),
                ('surname', models.CharField(max_length=250, unique=True)),
                ('email', models.CharField(max_length=250)),
                ('phone_number', models.IntegerField()),
                ('password', models.CharField(max_length=250, unique=True)),
                ('city', models.CharField(max_length=250)),
                ('street', models.CharField(max_length=250)),
                ('PCS', models.CharField(max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Quiz_answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=250, verbose_name='Answer')),
                ('verify', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)], verbose_name='0-false or 1-true')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.FloatField(blank=True, default=0, help_text='Enter between 1 - 5', null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('book', models.ManyToManyField(to='DatabaseApps.book')),
                ('profile', models.ManyToManyField(to='DatabaseApps.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Quiz_question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=250, verbose_name='Question')),
                ('delete2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='delete_answers', to='DatabaseApps.quiz_answer')),
                ('quizAnswer', models.ManyToManyField(to='DatabaseApps.quiz_answer')),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('delete1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='delete_question', to='DatabaseApps.quiz_question')),
                ('quizQuestion', models.ManyToManyField(to='DatabaseApps.quiz_question')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.ManyToManyField(to='DatabaseApps.genre'),
        ),
    ]
