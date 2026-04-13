from django.shortcuts import render
from django.http import HttpRequest , HttpResponse
from .models import Services


def services_view(request:HttpRequest):
    services = Services.objects.all()
    return render(request,'service/home.html',{'services':services})


def health(request:HttpRequest):
    return HttpResponse('I am alive')