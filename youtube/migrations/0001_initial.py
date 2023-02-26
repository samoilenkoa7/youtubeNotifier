# Generated by Django 4.1.7 on 2023-02-23 14:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='YoutuberToCheck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channel_name', models.CharField(max_length=200)),
                ('channel_username', models.CharField(max_length=200)),
                ('channel_url', models.URLField()),
                ('channel_id', models.CharField(max_length=150, null=True)),
                ('subscribers', models.ManyToManyField(related_name='subscriptions', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('channel_name', 'id'),
            },
        ),
        migrations.CreateModel(
            name='YouTubeVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_id', models.CharField(max_length=150)),
                ('youtuber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='youtube.youtubertocheck')),
            ],
        ),
    ]