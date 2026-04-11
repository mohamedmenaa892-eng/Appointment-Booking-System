from django.contrib import admin
from . import models

@admin.register(models.Availability)
class AvailabilityAdmin(admin.ModelAdmin):
    list_display = ('get_day_display','start_time','end_time')

@admin.register(models.Appointments)
class Appintments(admin.ModelAdmin):
    list_display = ('user','service','phone','full_name','date','start_time','end_time','status','email','mes_result')

@admin.register(models.BookingWendowDays)
class BokingWendowDaysAdmin(admin.ModelAdmin):
    list_display = ('booking_window_days',)