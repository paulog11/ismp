# Generated by Django 2.0.1 on 2020-05-03 21:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogpost', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='body',
        ),
        migrations.RemoveField(
            model_name='blogpost',
            name='title',
        ),
    ]