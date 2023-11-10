from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab


#have looked a lot on this https://www.youtube.com/watch?v=vplXie0uOz8&list=PLLz6Bi1mIXhHKA1Szy2aj9Jbs6nw9fhNY&index=4
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_rest_api_tasks.settings')
app=Celery('django_rest_api_tasks')
app.conf.enable_utc = False

app.conf.update(timezone = 'Europe/Stockholm')

app.config_from_object(settings, namespace="CELERY")

#celery beat settings
app.conf.beat_schedule={
    
    'generateHTML-every-day-at-0':{
        'task': 'app_backend.tasks.generateRandomAndupdateHTML',
        'schedule': crontab(hour=0, minute=0),
    }
}

app.autodiscover_tasks()
app.task(bind=True)
def debug_task(self):
    print(f'request: {self.request!r}')