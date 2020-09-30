from django.contrib import admin

from pybo import models

admin.site.register(models.Question)
admin.site.register(models.Answer)
