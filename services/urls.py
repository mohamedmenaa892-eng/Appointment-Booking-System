from django.urls import path
from . import views

urlpatterns = [
    path('',views.services_view,name='services_view'),
    path('health/',views.health,name='health')
]
