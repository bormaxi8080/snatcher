# -*- coding: utf-8 -*-

import logging

from django.db import DatabaseError
from base_publisher import BasePublisher

from ..projects.models import AdProject, AdGroup, Ad

LOGGER = logging.getLogger(__name__)


def _on_publish_messages(messages, params):
    for message in messages:
        try:
            # Update MaiListRef state
            # maillist = MailList(message['id'])
            # maillist.state = classes.evalbot_utils.MailListStateHelper.by_name(
            #    classes.evalbot_utils.MAILLIST_STATE_PUBLISHED)
            # maillist.save(update_fields=['state'])
            LOGGER.debug('Message published successfully: {0}'.format(message))
        except DatabaseError as err:
            LOGGER.error('{0} Update error: {1}'.format(message, err))


# Active Tasks Publisher
class ActiveTasksPublisher(BasePublisher):

    def __init__(self, params, queue, routing_key, exchange=''):
        super().__init__(queue, routing_key, exchange)

        # Save parameters
        self._params = params

    def query(self, row_number=100):
        print('AAAAAAAAAAAA')
        # Get active ads
        qs = Ad.objects.filter(
            active=True,
            row_number=row_number)

        for ad in qs:
            # groups = AdGroup.objects.filter(
            #    id=ad.adgroup_id
            # )

            print(ad)

            # for group in groups:
            #    project = AdProject.objects.filter(
            #        id=group.project_id
            #    )
            # message={}
            # super().append_message(message)

    def publish(self):
        super().publish_messages(_on_publish_messages)
