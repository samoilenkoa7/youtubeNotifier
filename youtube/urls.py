from django.urls import path

from . import views


urlpatterns = [
    path('create-subscribe/', views.YoutuberListCreateAPIView.as_view(), name='list-create-youtube'),
    path('subscribe/<int:pk>/', views.SubscribeToYoutuberAPIView.as_view(), name='update-youtube'),
]
