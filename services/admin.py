from django.contrib import admin
from . import models

@admin.register(models.Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('name','duration','price')
    search_fields = ('name',)
    exclude = ('slug',)