from django.contrib import admin
from .models import Todo_table
# Register your models here.
class Todo_table_admin(admin.ModelAdmin):
    list_display=['title','category','deadline']

admin.site.register(Todo_table,Todo_table_admin)