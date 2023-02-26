from rest_framework import serializers

from django.contrib.auth import get_user_model

from .models import YoutuberToCheck
from notifications.youtube_api_service import YouTubeAPIService


User = get_user_model()


class YoutuberToCheckCreateSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        new_youtuber = super().create(validated_data)
        new_youtuber.subscribers.add(self.context['user'])
        youtube_api_service = YouTubeAPIService()
        channel_id, channel_name = youtube_api_service.get_channel_name_and_id_from_username(
            validated_data['channel_username']
        )
        new_youtuber.channel_id = channel_id
        new_youtuber.channel_name = channel_name
        new_youtuber.save()
        return new_youtuber

    class Meta:
        model = YoutuberToCheck
        fields = ('channel_url', 'channel_username')


class SubscribersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class SubscribeToYoutuberSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    subscribers = SubscribersSerializer(many=True)

    def update(self, **kwargs):
        print(self.context['user'])
        self.instance.subscribers.add(self.context['user'])
        self.instance.save()
        return self.instance

    class Meta:
        model = YoutuberToCheck
        fields = ('user', 'subscribers')
