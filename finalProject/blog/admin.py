from django.contrib import admin

# Register your models here.

from .models import Todo

class CustomTodo(admin.ModelAdmin):
    list_display = ("id","title","description")

admin.site.register(Todo,CustomTodo)