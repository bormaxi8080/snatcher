# -*- coding: utf-8 -*-

from django.db import models
from django_filters import FilterSet, ChoiceFilter


# VProxy Type Names
PROXY_TYPE_HTTP = 'HTTP'
PROXY_TYPE_SOCKS3 = 'SOCKS3'

PROXY_TYPES = {
    PROXY_TYPE_HTTP: 1,
    PROXY_TYPE_SOCKS3: 2
}

PROXY_TYPE_CHOICES = (
    (1, PROXY_TYPE_HTTP),
    (2, PROXY_TYPE_SOCKS3)
)


class ProxyTypeHelper(object):
    @staticmethod
    def by_name(name):
        return PROXY_TYPES[name]

    @staticmethod
    def by_id(type_id):
        for choice in PROXY_TYPE_CHOICES:
            if choice[0] == type_id:
                return choice[1]
        raise Exception('Unknown proxy type: {0}'.format(type_id))


class Proxy(models.Model):
    address = models.CharField(max_length=255, null=False)
    description = models.TextField(null=True)
    proxy_type = models.IntegerField(choices=PROXY_TYPE_CHOICES, null=False, default=1)
    enabled = models.BooleanField(null=False, default=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)

    def __str__(self):
        return self.address
