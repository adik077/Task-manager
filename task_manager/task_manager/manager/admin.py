from django.contrib import admin
from .models import Task


@admin.register(Task)
class TaskRegister(admin.ModelAdmin):
    list_display = ['author', 'date_added', 'deadline', 'is_active']
    list_filter = ['author','deadline']
