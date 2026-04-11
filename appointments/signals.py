from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Appointments
from django.core.mail import send_mail
from django.db import transaction


@receiver(pre_save,sender=Appointments)
def send_status_mail(sender,instance,**kwargs):
    
    if not instance.pk:
        return
    
    old = Appointments.objects.get(pk=instance.pk)
    
    if old.status == instance.status:
        return
    
    if instance.status == 'confirmed':
        subject = 'Confirmed'
        text = 'Your booking has been accepted'
    
    elif instance.status == 'rejected':
        subject = 'Rejected'
        text = 'Your booking has been rejected'
    else:
        return
    
    transaction(lambda:send_mail(
        subject,
        text,
        'mohamedmenaa892@gmail.com',
        [instance.email],
        fail_silently=False
        ))