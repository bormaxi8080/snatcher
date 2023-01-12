# -*- coding: utf-8 -*-

from __future__ import absolute_import
import os

from celery import Celery
from celery.schedules import crontab    # scheduler

from django.apps import apps

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'snatcher_admin.settings')

app = Celery('snatcher_admin')
app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()
# app.autodiscover_tasks(lambda: [n.name for n in apps.get_app_configs()])

app.conf.beat_schedule = {
    # executes every 1 minute
    'publish-active-tasks': {
       'task': 'snatcher_admin.tasks.publish_active_tasks',
       'schedule': crontab(),
    },
}
