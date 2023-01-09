from django.contrib import admin

from first_proj.models import Category, Event

# Register your models here.
admin.site.register(Category)
admin.site.register(Event)