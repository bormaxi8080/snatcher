from django.contrib import admin

# Register your models here.

from .models import Device
from .models import Format
from .models import Placement
from .models import Geo
from .models import AdProject
from .models import AdGroup
from .models import Ad

admin.site.register(Device)
admin.site.register(Format)
admin.site.register(Placement)
admin.site.register(Geo)
admin.site.register(AdProject)
admin.site.register(AdGroup)
admin.site.register(Ad)
