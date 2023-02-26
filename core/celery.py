import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('core')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'everyday-5-minutes': {
      'task': 'notifications.tasks.check_new_videos',
      'schedule': crontab(minute='*/1')
    }
}
