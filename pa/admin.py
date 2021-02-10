

from django.contrib import admin
from .models import *

@admin.register(Tasks)
class TasksAdmin(admin.ModelAdmin):
    list_display = ('task',)
