from django.contrib import admin
from auth_app import models

# Register your models here.

admin.site.register(models.UserProfile)
admin.site.register(models.Shows)