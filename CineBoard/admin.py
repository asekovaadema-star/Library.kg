from django.contrib import admin
from . import models

admin.site.register(models.CinemaModel)
admin.site.register(models.Genre)
admin.site.register(models.Comment)
admin.site.register(models.VIPReservation)

