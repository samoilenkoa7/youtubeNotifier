import logging

import requests

from django.conf import settings


logger = logging.getLogger('notifications')


class YouTubeAPIService:
    def __init__(self):
        self.base_url = settings.YOUTUBE_API_URL
        self.api_key = settings.YOUTUBE_API_KEY

    def get_channel_name_and_id_from_username(self, username: str) -> tuple[str, str]:
        params = {
            'forUsername': username,
            'key': self.api_key,
            'part': 'snippet',
            'order': 'date'
        }
        response = requests.get(self.base_url + '/youtube/v3/channels', params=params)
        channel_items = response.json()
        channel_items = channel_items.get('items')[0]
        channel_snippet = channel_items.get('snippet')
        channel_name = channel_snippet.get('title')
        channel_id = channel_items.get('id')
        return channel_id, channel_name

    def get_last_channel_videos(self, channel):
        params = {
            'key': self.api_key,
            'part': 'snippet',
            'channelId': channel.channel_id,
            'order': 'date'}
        response = requests.get(self.base_url + '/youtube/v3/search', params=params)

        channel_items = response.json()
        channel_items = channel_items.get('items')
        return channel_items
