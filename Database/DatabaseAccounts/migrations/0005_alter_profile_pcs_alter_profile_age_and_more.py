# Generated by Django 4.1.2 on 2022-12-21 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DatabaseAccounts', '0004_alter_profile_pcs_alter_profile_age_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='PCS',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
    ]
