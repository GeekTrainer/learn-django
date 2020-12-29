from django.contrib import admin

# [TODO] Register models.
from .models import Shelter, Dog

admin.site.register(Shelter)
admin.site.register(Dog)