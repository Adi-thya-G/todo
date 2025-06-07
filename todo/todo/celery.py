from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from django.conf import settings
from celery.schedules import crontab
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todo.settings')

app = Celery('todo')
app.conf.enable_utc = False

app.conf.update(timezone = 'Asia/Kolkata')

app.config_from_object(settings, namespace='CELERY')
app.autodiscover_tasks()

# Celery Beat Settings
app.conf.beat_schedule = {
    'send-reminders-every-minute': {
        'task': 'send_mail_app.tasks.send_mail_func',
        'schedule': crontab(minute='*'),  # Runs every minute
    },
}
