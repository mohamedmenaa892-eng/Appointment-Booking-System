from django.urls import path
from . import views

urlpatterns = [
    path('service/<slug:slug>/',views.booking_days,name="booking_days"),
    path('service/<slug:slug>/<str:date>/',views.time_slot_view,name='booking_slots'),
    path('service/<slug:slug>/<str:time>/<str:date>',views.appointments,name='confirme_booking')
]


