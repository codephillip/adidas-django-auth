# Generated by Django 3.2.4 on 2022-03-19 03:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adidas_django_auth', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='dob',
        ),
    ]