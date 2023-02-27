from django.contrib.auth import get_user_model

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView

from rest_framework.permissions import IsAuthenticated

from .models import Profile
from .serializers import RegistrationSerializer, ProfileEmailUpdateSerializer, ProfileUpdateTelegramIDSerializer \
                        , ProfileUpdatePreferredMethodSerializer


User = get_user_model()


class RegisterUserAPIView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer


class ChangeEmailAddressAPIView(RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ProfileEmailUpdateSerializer
    http_method_names = ['patch', 'get']


class ChangeTelegramIDAPIView(RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ProfileUpdateTelegramIDSerializer
    http_method_names = ['patch', 'get']


class ChooseDefaultNotificationMethodAPIView(RetrieveUpdateAPIView):
    lookup_url_kwarg = 'email'
    lookup_field = 'email'

    queryset = Profile.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ProfileUpdatePreferredMethodSerializer
    http_method_names = ['patch', 'get']
