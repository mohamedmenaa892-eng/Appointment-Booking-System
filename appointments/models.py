from django.db import models
from django.conf import settings
from services.models import Services


class Availability(models.Model):
    day = models.IntegerField(choices=[
        (0,'Monday'),
        (1,'Tuesday'),
        (2,'wednesday'),
        (3,'Thursday'),
        (4,'Friday'),
        (5,'Saturday'),
        (6,'Sunday'),
    ])
    start_time = models.TimeField()
    end_time = models.TimeField()


class Appointments(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    service = models.ForeignKey(Services,on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    full_name = models.CharField(max_length=30)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    status = models.CharField(
        max_length=30,
        choices=[
            ('pending','Pending'),
            ('confirmed','Confirmed'),
            ('rejected','Rejected')
        ],
        default='Pending')
    email = models.EmailField(null=True,blank=True)
    mes_result = models.TextField(null=True,blank=True)
    
    
    class Meta:
        ordering = ['-date','start_time']
        constraints = [
            models.UniqueConstraint(
            fields=['date','start_time'],
            name='date_time'
        )]


class BookingWendowDays(models.Model):
    booking_window_days = models.PositiveIntegerField(default=14)