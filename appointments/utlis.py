from datetime import datetime , timedelta , date
from .models import Availability , Appointments , BookingWendowDays


# Funtion view booking days
def view_days(service):
    
    days_list = []
    
    today = date.today()
    window = BookingWendowDays.objects.first()
    window_date = window.booking_window_days if window else 14
    max_days = today + timedelta(days=window_date)
    
    today_varuble = today
    
    availability_num = list(Availability.objects.values_list('day',flat=True))
    
    while today_varuble <= max_days:
        day_number = today_varuble.weekday()
        if day_number in availability_num :
            slots = generate_time_slots(today_varuble,service)
            slots_ = validate_slots(slots,today_varuble,service)
            if slots_ :
                days_list.append(today_varuble)
        today_varuble += timedelta(days=1)
    
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


