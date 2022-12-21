# -*- coding: utf-8 -*-

import logging
import pika
import pika.exceptions


LOGGER = logging.getLogger(__name__)


class SyncPikaPublisher(object):

    def __init__(self, username='guest', password='guest', host='localhost', port=5672,
                 durable=False, confirm_delivery=False, delivery_mode=2, mandatory=False):
        # delivery_mode=2 - Make message persistent
        self._username = username
        self._password = password
        self._host = host
        self._port = port

        self._durable = durable
        self._confirm_delivery = confirm_delivery
        self._delivery_mode = delivery_mode
        self._mandatory = mandatory

        self._credentials = pika.PlainCredentials(username=self._username, password=self._password)
        self._parameters = pika.ConnectionParameters(host=self._host, port=self._port,
                                                     credentials=self._credentials)
        self._connection = pika.BlockingConnection(self._parameters)

    def __del__(self):
        if self._connection.is_open:
            self._connection.close()

    def get_amqp_url(self):
        # AMQP_URL = 'amqp://guest:guest@localhost:5672/%2F'
        return 'amqp://{0}:{1}@{2}:{3}/'.format(self._username, self._password, self._host, self._port)

    def publish_message(self, body, queue, routing_key, exchange=''):
        channel = self._connection.channel()
        try:
            # Declare queue
            channel.queue_declare(queue=queue, durable=self._durable)

            if self._confirm_delivery:
                # Turn on delivery confirmations
                channel.confirm_delivery()

            # Set basic properties
            properties = pika.BasicProperties(delivery_mode=self._delivery_mode)
            try:
                # Publish message in queue
                channel.basic_publish(exchange=exchange, routing_key=routing_key, body=body,
                                      properties=properties, mandatory=self._mandatory)
            except pika.exceptions.UnroutableError:
                LOGGER.warning('{0} Message publish could not be confirmed'.format(body))
                raise
            except Exception as err:
                LOGGER.error('{0} Message publish error: {1}'.format(body, err))
                raise

        finally:
            if channel.is_open:
                channel.close()
