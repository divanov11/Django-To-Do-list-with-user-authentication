from django.contrib import admin
from .models import Task

# Registered the model in admin to show the table in admin panel
admin.site.register(Task)
