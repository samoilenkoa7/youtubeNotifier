from celery import shared_task

from youtube.models import YoutuberToCheck

from notifications.services import YouTubeNotificationService


@shared_task
def check_new_videos():
    youtube_api_service = YouTubeNotificationService()
    for channel in YoutuberToCheck.objects.all():
        youtube_api_service.check_channel_videos(channel)
