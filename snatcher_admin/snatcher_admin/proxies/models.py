from django.db import models


class Proxy(models.Model):
    address = models.CharField(max_length=255, null=False)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.address
