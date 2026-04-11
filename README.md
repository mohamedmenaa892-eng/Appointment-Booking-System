# Booking System (Django)

## Overview

This is a Django-based appointment booking system that allows users to view available days, select time slots, and book services without overlapping existing appointments. It includes availability management, booking window restrictions, and automated email notifications for booking status updates.

---

## Features

* Service-based appointment booking
* Dynamic available days calculation
* Time slot generation based on service duration
* Overlap prevention (no double booking)
* Booking window limitation (e.g., next 14 days)
* User authentication required for booking
* Appointment status management (pending / confirmed / rejected)
* Email notifications on status change

---

## Tech Stack

* Python 3.x
* Django
* SQLite / PostgreSQL (optional)
* Bootstrap (frontend UI)
* Django Signals (email notifications)

---

## Models

### Availability

Defines working days and working hours.

* day: weekday (0 = Monday ... 6 = Sunday)
* start_time: working start time
* end_time: working end time

---

### Appointments

Stores booked appointments.

* user: linked user
* service: booked service
* phone: contact number
* full_name: customer name
* date: appointment date
* start_time: start time
* end_time: end time
* status: pending / confirmed / rejected
* email: notification email
* mes_result: optional message

**Constraints:**

* UniqueConstraint on (date, start_time) to avoid duplicates

**Ordering:**

* Latest date first, then start_time

---

### BookingWindowDays

Controls how far users can book in advance.

* booking_window_days (default = 14)

---

## Booking Flow

1. User selects a service
2. System displays available days (`view_days`)
3. User selects a date
4. System generates time slots (`generate_time_slots`)
5. System filters overlapping bookings (`validate_slots`)
6. User confirms booking
7. Appointment is saved with status = pending

---

## Utility Functions

### view_days(service)

Returns a list of available booking dates based on:

* Availability table
* Booking window limit
* Existing valid time slots

---

### generate_time_slots(date, service)

Generates time slots based on:

* Availability hours
* Service duration

---

### validate_slots(slots, date, service)

Removes overlapping slots by checking existing appointments.

---

## Views

### booking_days

Displays available booking dates for a service.

### time_slot_view

Shows available time slots for a selected date.

### appointments (confirm booking)

* Requires login
* Validates slot availability
* Saves booking
* Calculates end time using service duration

---

## Signals

### send_status_mail (pre_save)

Automatically sends email when appointment status changes:

* Confirmed → acceptance email
* Rejected → rejection email

---

## Bootstrap Pages (UI Structure)

### Suggested Pages

#### 1. booking_days.html

* Grid of available dates
* Each date is a clickable Bootstrap card or button

#### 2. time_slots.html

* Displays available time slots as buttons
* Disabled style for unavailable slots
* Responsive grid layout (Bootstrap row/col)

#### 3. confirm_booking.html

* Booking confirmation form
* Service info summary (name, date, time)
* Bootstrap form styling

---

## Example UI Structure (Bootstrap)

* Navbar (service name / user login)
* Cards for services
* Buttons for dates and time slots
* Forms styled with `form-control` and `btn btn-primary`
* Alerts for success/error messages

---

## Settings Required

### Email (required for signals)

Make sure Django email backend is configured:

* EMAIL_HOST
* EMAIL_PORT
* EMAIL_HOST_USER
* EMAIL_HOST_PASSWORD
* DEFAULT_FROM_EMAIL

---

## Notes

* Ensure `Availability` is filled before using booking system
* Ensure at least one service exists with duration field
* Signal depends on email being valid in appointment model
* Overlap prevention is handled both in Python and DB constraint

---

## Future Improvements

* Add cancellation system
* Add admin dashboard analytics
* Add timezone support
* Add payment integration
* Add real-time slot updates (AJAX)

---

## Author

Django Booking System Project
