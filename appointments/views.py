from django.shortcuts import render , get_object_or_404 , redirect
from django.http import HttpRequest
from services.models import Services
from datetime import timedelta , datetime
from .utlis import generate_time_slots , validate_slots , view_days
from .forms import FormBooking
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.contrib import messages



def booking_days(request:HttpRequest , slug):
    service = get_object_or_404(Services , slug=slug)
    
    days_list = view_days(service)
    
    context = {
        'service':service,
        'days_list':days_list
    }
    
    return render(request,'appointments/booking_days.html', context)



def time_slot_view(request:HttpRequest , slug , date ):
    
    service = get_object_or_404(Services,slug=slug)
    selecte_date = datetime.strptime(date , '%Y-%m-%d').date()
    
    slots = generate_time_slots(selecte_date , service)
    slots_ = validate_slots(slots,selecte_date,service)
    
    context = {
        'service':service,
        'slots':slots_,
        'day':selecte_date
    }
    
    return render(request,'appointments/time_slots.html',context)


@login_required()
def appointments(request: HttpRequest, slug, time, date):
    
    form = FormBooking(request.POST or None)
    service = get_object_or_404(Services, slug=slug)
    
    day = datetime.strptime(date, '%Y-%m-%d').date()
    
    start_time = datetime.strptime(time, '%H:%M').time()
    
    time_now = datetime.combine(day, start_time)
    duration = timedelta(minutes=service.duration)
    end_time = (time_now + duration).time()
    
    slots = generate_time_slots(day,service)
    slots_ = validate_slots(slots,day,service)
    if start_time not in slots_:
        return redirect('booking_slots', slug=slug , date=date)
        
    if request.method == 'POST' and form.is_valid():
        
        booking = form.save(commit=False)
        booking.user = request.user
        booking.service = service
        booking.date = day
        booking.start_time = start_time
        booking.end_time = end_time
        
        # save booking
        try:
            booking.save()
            messages.success(request,
                            '''
                            Your appointment has been successfully booked.
                            A confirmation or rejection message will be sent 
                            to the email you provided
                            ''')
            return redirect('services_view')
            
        except IntegrityError:
            return redirect('confirme_booking')
    
    context = {
        'form': form,
        'service':service,
        'day':day,
        'start_time':start_time,
        'end_time':end_time
        
    }
    
    return render(request, 'appointments/confirme_booking.html', context)