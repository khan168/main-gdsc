from django.contrib import admin
# Register your models here.
from .models import Note, profiles

admin.site.register(Note)
admin.site.register(profiles)