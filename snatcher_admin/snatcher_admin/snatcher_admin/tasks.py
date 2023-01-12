# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from django.conf import settings
from celery import shared_task
from celery.utils.log import get_task_logger

# from ..publishers.active_tasks_publisher import ActiveTasksPublisher

LOGGER = get_task_logger(__name__)


@shared_task(serializer='json')
def publish_active_tasks():
    print('BBBBBBBBBB')
    # publisher = ActiveTasksPublisher(
    #    params=None,
    #    queue=settings.QUEUE_ACTIVE_TASKS,
    #    routing_key=settings.ROUNTING_KEY_ACTIVE_TASKS
    #)
    # publisher.query(row_number=100)
    # publisher.publish()
