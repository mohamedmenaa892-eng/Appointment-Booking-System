from django.urls import path 
from . import views

app_name = 'user_auth'

urlpatterns =[
    path('login/',views.login_,name='login'),
    path('create_account/',views.CreateAccount.as_view(),name='create_account'),
    path('logout/',views.logout_,name='logout'),
]