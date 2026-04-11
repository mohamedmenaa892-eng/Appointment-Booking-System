from django.shortcuts import render , redirect
from django.http import HttpRequest 
from .form import LoginForm , CreateAccountForm
from django.contrib.auth import login , logout
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib import messages


def login_(request:HttpRequest):
    
    form = LoginForm(request.POST or None)
    next_url = request.GET.get('next') or request.POST.get('next')
    
    if request.method == 'POST':
        if form.is_valid():
            login(request,form.user)
            if next_url :
                return redirect(next_url)
            
            return redirect('services_view')
    return render(request,'main/login.html',{
        'form':form
        })

class CreateAccount(CreateView):
    form_class = CreateAccountForm
    template_name = 'main/create_account.html'
    success_url = reverse_lazy('login')


def logout_(request:HttpRequest):
    logout(request)
    messages.success(request,'You have been logged out successfully')
    return redirect('services_view')