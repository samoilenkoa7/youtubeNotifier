from django.contrib.auth import get_user_model

from rest_framework.generics import ListCreateAPIView

from .serializers import RegistrationSerializer


User = get_user_model()


class RegisterUserAPIView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer
