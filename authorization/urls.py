from django.urls import path

from rest_framework.authtoken.views import ObtainAuthToken

from .views import RegisterUserAPIView, ChangeEmailAddressAPIView, ChangeTelegramIDAPIView,\
    ChooseDefaultNotificationMethodAPIView


urlpatterns = [
    path('register/', RegisterUserAPIView.as_view(), name='register'),
    path('login/', ObtainAuthToken.as_view(), name='login'),
    path('change-email/<int:pk>/', ChangeEmailAddressAPIView.as_view(), name='change-email'),
    path('change-telegram/<int:pk>/', ChangeTelegramIDAPIView.as_view(), name='change-telegram'),
    path('change-method/<str:email>/', ChooseDefaultNotificationMethodAPIView.as_view(), name='default-method')
]
