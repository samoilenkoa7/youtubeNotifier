# Generated by Django 4.1.7 on 2023-02-27 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authorization', '0002_profile_preferred_contact_method'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(default='samoilenkoa7@gmail.com', max_length=254, unique=True),
        ),
    ]