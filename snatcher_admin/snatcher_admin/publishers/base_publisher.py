# -*- coding: utf-8 -*-

import json
import logging

from ..classes.sync_pika_publisher import SyncPikaPublisher
from django.conf import settings

LOGGER = logging.getLogger(__name__)


class BasePublisher(object):

    def __init__(self, queue, routing_key, exchange=''):
        self._messages = []
        self._params = None
        self._queue = queue
        self._exchange = exchange
        self._routing_key = routing_key
        self._publisher = SyncPikaPublisher(username=settings.CELERY_BROKER_USER,
                                            password=settings.CELERY_BROKER_PASSWORD,
                                            host=settings.CELERY_BROKER_HOST,
                                            port=settings.CELERY_BROKER_PORT,
                                            durable=True,
                                            confirm_delivery=True)

    def append_message(self, message):
        self._messages.append(message)

    def get_messages(self):
        return self._messages

    def publish_messages(self, on_messages_publish_callback):
        self._publish_message(self._messages, on_messages_publish_callback)

    def publish_messages_separately(self, on_message_publish_callback):
        for message in self._messages:
            self._publish_message(message, on_message_publish_callback)

    def _publish_message(self, message, on_message_publish_callback):
        # Publish message to queue
        self._publisher.publish_message(queue=self._queue,
                                        exchange=self._exchange,
                                        routing_key=self._routing_key,
                                        body=json.dumps(message))
        # Calling the callback
        on_message_publish_callback(message, self._params)
