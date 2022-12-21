from django.db import models


class Account(models.Model):
    site = models.URLField(null=False)
    login = models.CharField(max_length=255, null=False)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)

    def __str__(self):
        return '{0}: {1}'.format(self.site, self.login)
