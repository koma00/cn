# Generated by Django 3.0.2 on 2020-02-01 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='sex',
            field=models.CharField(choices=[('male', 'male'), ('female', 'female')], default='male', max_length=20),
        ),
    ]
