from django import forms
from .models import Appointments


class FormBooking(forms.ModelForm):
    
    class Meta:
        model = Appointments
        fields = ['phone','full_name','email']
        wedget = {
            'full_name':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Enter the full name ....',
            }),
            
            'phone':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Enter the number phone...'
            }),
            
            'email':forms.EmailInput(attrs={
                'class':'form-control',
                'placeholder':'Enter the email...'
            }),
        }