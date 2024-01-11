# Generated by Django 4.2 on 2024-01-08 20:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(error_messages={'unique': 'A User with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.core.validators.RegexValidator('^[a-zA-Z][a-zA-Z0-9_\\.]+&', 'Enter a valid username. This value may contain only letters, numbers and @ characters.', 'invalid')]),
        ),
    ]