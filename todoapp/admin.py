from django.contrib import admin
from .models import Todo
# Register your models here.
class TodoAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "tasks", "date_created", "deadline", "status")

admin.site.register(Todo, TodoAdmin)