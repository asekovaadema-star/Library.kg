from django.contrib import admin
from . import models

admin.site.register(models.Location)
admin.site.register(models.Reservation)
admin.site.register(models.CommentLocation)
admin.site.register(models.CategoryHorse)
