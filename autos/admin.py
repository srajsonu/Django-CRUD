from django.contrib import admin

# Register your models here.
from autos import models

admin.site.register(models.Auto)
admin.site.register(models.Make)
