from datetime import datetime , timedelta , date 
from .models import Availability , Appointments , BookingWendowDays
from django.utils import timezone




def view_days(service):
    days_list = []
    today = date.today()
    window = BookingWendowDays.objects.first()
    window_date = window.booking_window_days if window else 14
    max_days = today + timedelta(days=window_date)
    
    availability_num = list(Availability.objects.values_list('day', flat=True))
    
    today_current = today
    now = timezone.now().time()
    
    while today_current <= max_days:
        
        day_number = today_current.weekday()
        if day_number in availability_num:
            
            availability = Availability.objects.filter(day=day_number).first()
            
            if today_current == today:
                start_time = availability.start_time
                end_time = availability.end_time
                is_available = start_time <= now <= end_time if start_time <= end_time else (start_time <= now or now <=end_time)
            else:
                is_available = True
            
            if is_available :
                
                slots = generate_time_slots(today_current,service)
                slots_ = validate_slots(slots,today_current,service)
                
                if slots_:
                    days_list.append(today_current)
        
        today_current += timedelta(days=1)
        
    return days_list




# Function view booking slots
def generate_time_slots(selecte_date , service):
    
    slots = []
    
    day_number = selecte_date.weekday()
    availability_day = Availability.objects.filter(day=day_number).first()
    
    if not availability_day:
        return []
    
    start_time = availability_day.start_time
    end_time = availability_day.end_time
    
    time_now = datetime.combine(selecte_date,start_time)
    end = datetime.combine(selecte_date,end_time)
    
    duration = timedelta(minutes=service.duration)
    
    while time_now + duration <= end :
        slots.append(time_now.time())
        time_now += duration
    
    return slots



# Function validate booking slots  ( overlap )
def validate_slots(slots,selecte_date,service):
    
    slots_ = []
    
    
    bookings = Appointments.objects.filter(date=selecte_date)
    duration = timedelta(minutes=service.duration)
    
    for slot in slots:
        overlap = False
        
        start_slot = datetime.combine(selecte_date,slot)
        end_slot = start_slot + duration
        
        for booking in bookings:
            start_booking = datetime.combine(selecte_date,booking.start_time)
            end_booking = datetime.combine(selecte_date,booking.end_time)
            
            if start_slot < end_booking and end_slot > start_booking:
                overlap = True
                break
        if not overlap :
            slots_.append(slot)
    
    return slots_


