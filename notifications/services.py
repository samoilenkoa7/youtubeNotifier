import logging

import requests

from django.conf import settings
from django.contrib.auth import get_user_model

from django.core.mail import send_mail

from youtube.models import YoutuberToCheck

User = get_user_model()

logger = logging.getLogger('notifications')


class TelegramService:
    def __init__(self):
        self.base_url = settings.TELEGRAM_API_URL
        self.bot_token = settings.TELEGRAM_API_BOT_TOKEN

    def send_tg_notification(self, user: User, new_video: str, youtuber):
        chat_id = user.profile.telegram_username
        message = settings.MESSAGE_TEMPLATE.format('Subscriber', youtuber.channel_name,
                                                   settings.BASE_YOUTUBE_VIDEO_URL.format(new_video))
        url_req = self.base_url + '/bot' + self.bot_token + "/sendMessage" + "?chat_id=" + chat_id \
                  + "&text=" + message + '&parse_mode=HTML'
        response = requests.post(url_req)
        logger.info(msg=f'Sending message to {user.username}, status of request: {response.status_code}')


class EmailService:
    def __init__(self):
        self.sender = settings.EMAIL_HOST_USER
        self.message = settings.MESSAGE_TEMPLATE

    def send_email_to_subscribers(self, receiver: str, youtuber: YoutuberToCheck, new_video: str):
        self.message = self.message.format('Subscriber', youtuber.channel_name,
                                                        settings.BASE_YOUTUBE_VIDEO_URL.format(new_video))
        send_mail('NEW Youtube Video is out!', self.message, self.sender, [receiver])


class YouTubeNotificationService:
    def __init__(self):
        from notifications.youtube_api_service import YouTubeAPIService

        self.youtube_api_service: YouTubeAPIService = YouTubeAPIService()
        self.telegram_service: TelegramService = TelegramService()
        self.email_servie: EmailService = EmailService()

    def check_channel_videos(self, channel):
        from youtube.models import YouTubeVideo
        channel_items = self.youtube_api_service.get_last_channel_videos(channel)
        all_saved_videos = YouTubeVideo.objects.filter(youtuber__channel_id=channel.channel_id).values('video_id')
        all_videos = [video_id for video in all_saved_videos for video_id in video.values()]
        for item in channel_items:
            video_id = item.get('id').get('videoId')
            if video_id not in all_videos:
                YouTubeVideo.objects.create(video_id=video_id, youtuber_id=channel.id)
                logger.info(msg=f'Starting sending notification to subscribers of: {channel}')
                self._send_notifications_to_all_subscribers(channel, video_id)

    def _send_notifications_to_all_subscribers(self, channel,
                                               video_id: str):
        for subscriber in channel.subscribers.select_related('profile'):
            if subscriber.profile.preferred_contact_method == 'tg':
                logger.info(f'Starting sending telegram message for video {video_id}')
                self.telegram_service.send_tg_notification(subscriber, video_id, channel)
            else:
                self.email_servie.send_email_to_subscribers(subscriber.email, channel, video_id)
