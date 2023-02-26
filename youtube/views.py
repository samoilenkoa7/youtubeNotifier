from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import YoutuberToCheck
from .serializers import YoutuberToCheckCreateSerializer, SubscribeToYoutuberSerializer


class YoutuberListCreateAPIView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = YoutuberToCheck.objects.all()
    serializer_class = YoutuberToCheckCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={'user': request.user})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class SubscribeToYoutuberAPIView(RetrieveUpdateAPIView):
    queryset = YoutuberToCheck.objects.all()
    serializer_class = SubscribeToYoutuberSerializer
    permission_classes = (IsAuthenticated,)

    def put(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           instance=self.get_object(),
                                           context={'user': request.user})
        serializer.update()
        return Response({'Successfully subscribed!!!!'}, status=201)
