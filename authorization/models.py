from django.db import models
from django.db.models.signals import post_save

from django.dispatch import receiver
from django.contrib.auth import get_user_model


User = get_user_model()


class Profile(models.Model):
    PREFERRED_CONTACT_TYPES = (
        ('Telegram', 'tg'),
        ('Email', 'email')
    )

    telegram_username = models.CharField(max_length=120, unique=True, null=True)
    email = models.EmailField(default='samoilenkoa7@gmail.com', unique=True)
    is_telegram_notifications = models.BooleanField(default=True)
    is_email_notifications = models.BooleanField(default=False)
    preferred_contact_method = models.CharField(choices=PREFERRED_CONTACT_TYPES, max_length=10, default='tg')
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, *args, **kwargs):
    if created:
        Profile.objects.create(user=instance, email=instance.email)
