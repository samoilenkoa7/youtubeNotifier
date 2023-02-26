from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class YoutuberToCheck(models.Model):
    """
    Model of youtubers which can create users to receive notifications
    about new content
    """
    channel_name = models.CharField(max_length=200)
    channel_username = models.CharField(max_length=200)
    channel_url = models.URLField()
    channel_id = models.CharField(max_length=150, null=True)
    subscribers = models.ManyToManyField(User, related_name='subscriptions')

    def __str__(self):
        return f'{self.channel_name}'

    class Meta:
        ordering = ('channel_name', 'id')


class YouTubeVideo(models.Model):
    youtuber = models.ForeignKey('YoutuberToCheck', related_name='videos', on_delete=models.CASCADE)
    video_id = models.CharField(max_length=150)

    def __str__(self):
        return f'{self.video_id}, {self.youtuber}'
