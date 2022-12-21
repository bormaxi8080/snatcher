from django.db import models
# from django_filters import FilterSet, ChoiceFilter

import uuid

# Format Names
FORMAT_BANNERS = 'banners'

# Formats
FORMATS = {
    FORMAT_BANNERS: 1
}

# Format Choices
FORMAT_CHOICES = (
    (1, FORMAT_BANNERS)
)

# Device Names
DEVICE_DESKTOP_MOBILE_WEB = 'desktop/mobile-web'

# Devices
DEVICES = {
    DEVICE_DESKTOP_MOBILE_WEB: 1
}

# Device Choices
DEVICE_CHOICES = (
    (1, DEVICE_DESKTOP_MOBILE_WEB)
)

# Placement Names
PLACEMENT_AUDITORIUM_PURCHASES = 'Auditorium Purchases'

# Placements
PLACEMENTS = {
    PLACEMENT_AUDITORIUM_PURCHASES: 1
}

# Placement Choices
PLACEMENT_CHOICES = (
    (1, PLACEMENT_AUDITORIUM_PURCHASES)
)


# Placement model
class Placement(models.Model):
    name = models.CharField(max_length=255, null=False, unique=True)
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)

    def __str__(self):
        return self.name


# Device model
class Device(models.Model):
    name = models.CharField(max_length=255, null=False, unique=True)
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)

    def __str__(self):
        return self.name


# Format model
class Format(models.Model):
    name = models.CharField(max_length=255, null=False, unique=True)
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)

    def __str__(self):
        return self.name


# Geo model
class Geo(models.Model):
    name = models.CharField(max_length=255, null=False, unique=True)
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)

    def __str__(self):
        return self.name


# AdProject model
class AdProject(models.Model):
    uid = models.UUIDField(auto_created=True, null=False, default=uuid.uuid4)
    project_name = models.CharField(max_length=255, null=False, default='')
    start_date = models.DateTimeField(null=False)
    end_date = models.DateTimeField(null=False)
    active = models.BooleanField(null=False, default=True)
    device_id = models.ForeignKey(Device, on_delete=models.CASCADE)
    format_id = models.ForeignKey(Format, on_delete=models.CASCADE)
    placement_id = models.ForeignKey(Placement, on_delete=models.CASCADE)
    geo_id = models.ForeignKey(Geo, on_delete=models.CASCADE)
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)

    def __str__(self):
        return self.project_name


# AdGroup model
class AdGroup(models.Model):
    uid = models.UUIDField(auto_created=True, null=False, default=uuid.uuid4)
    group_name = models.CharField(max_length=255, null=False, default='')
    project_id = models.ForeignKey(AdProject, on_delete=models.CASCADE)
    active = models.BooleanField(null=False, default=True)
    roboticity = models.IntegerField(null=False)
    br = models.IntegerField(null=False)
    depth = models.IntegerField(null=False)
    timing = models.IntegerField(null=False)
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)

    def __str__(self):
        return self.group_name


# Ad model
class Ad(models.Model):
    uid = models.UUIDField(auto_created=True, null=False, default=uuid.uuid4)
    ad_name = models.CharField(null=False, max_length=255, default='')
    adgroup_id = models.ForeignKey(AdGroup, on_delete=models.CASCADE)
    active = models.BooleanField(null=False, default=True)
    clicks = models.IntegerField(null=False)
    url = models.URLField(null=False)
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)

    def __str__(self):
        return self.ad_name
