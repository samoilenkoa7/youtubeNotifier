# Generated by Django 4.1.7 on 2023-02-20 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authorization', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='preferred_contact_method',
            field=models.CharField(choices=[('Telegram', 'tg'), ('Email', 'email')], default='tg', max_length=10),
        ),
    ]
