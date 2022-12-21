# -*- coding: utf-8 -*-

import logging
import pika

LOGGER = logging.getLogger(__name__)


class SyncPikaConsumer(object):

    def __init__(self, username='guest', password='guest', host='localhost', port=5672, durable=True,
                 chunk_size=0, prefetch_count=16):
        self._username = username
        self._password = password
        self._host = host
        self._port = port

        self._durable = durable
        self._chunk_size = chunk_size
        self._prefetch_count = prefetch_count

        self._credentials = pika.PlainCredentials(username=username, password=password)
        self._parameters = pika.ConnectionParameters(host=host, port=port, credentials=self._credentials)
        self._connection = pika.BlockingConnection(self._parameters)

    def __del__(self):
        if self._connection.is_open:
            self._connection.close()

    def get_amqp_url(self):
        # AMQP_URL = 'amqp://guest:guest@localhost:5672/%2F'
        return 'amqp://{0}:{1}@{2}:{3}/'.format(self._username, self._password, self._host, self._port)

    def get_chunk_size(self):
        return self._chunk_size

    def set_chunk_size(self, size):
        self._chunk_size = size

    # noinspection PyTypeChecker
    def consume_messages(self, queue, params, handle_message_callback):
        channel = self._connection.channel()
        try:
            # Declare queue
            channel.queue_declare(queue=queue, durable=self._durable)
            # Set prefetch count
            channel.basic_qos(prefetch_count=self._prefetch_count)

            for method_frame, properties, body in channel.consume(queue=queue):
                LOGGER.debug('Consume message: {0}'.format(body))

                try:
                    # Message processing here
                    handle_message_callback(method_frame, properties, body, params)
                except Exception as err:
                    LOGGER.error('{0} Error consuming message. ERROR: {1}'.format(body, err))
                finally:
                    # Acknowledge the message in any case!
                    channel.basic_ack(method_frame.delivery_tag)

                if self._chunk_size > 0:
                    # Escape out of the loop after chunk_size messages
                    if method_frame.delivery_tag > self._chunk_size:
                        break

            # Cancel the consumer and return any pending messages
            requeued_messages = channel.cancel()
            LOGGER.debug('Requeued {0} message(s)'.format(requeued_messages))
        finally:
            if channel.is_open:
                channel.close()
