from django.contrib import admin

# Register your models here.
from .models import VendorForm
admin.site.register(VendorForm)

from .models import visitform
admin.site.register(visitform)