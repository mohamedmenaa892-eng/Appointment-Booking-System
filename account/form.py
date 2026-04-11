from django import forms
from django.contrib.auth import authenticate 
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

User = get_user_model()

class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            "class": "form-control",
            "placeholder": "Enter your email"
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Enter your password"
        })
    )
    
    def clean(self):
        clean_data = super().clean()
        email = clean_data.get('email')
        password = clean_data.get('password')
        user = authenticate(email=email,password=password)
        if user is None:
            raise forms.ValidationError('Invalid credentials')
        self.user = user
        return clean_data


class CreateAccountForm(forms.ModelForm):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class':'form-control',
            'placeholder':'Enter your email'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class':'form-control',
            'placeholder':'Enter your password'
        }))
    password_confirme = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class':'form-control',
            'placeholder':'confirme password'
        })
        )
    
    class Meta:
        model = User
        fields = ['email','password']
    
    def clean_password(self):
        password = self.cleaned_data.get('password')
        try:
            validate_password(password)
        except ValidationError as e :
            raise forms.ValidationError(e.messages)
        return password
    
    def clean(self):
        clean_data = super().clean()
        password = clean_data.get('password')
        password_confirme = clean_data.get('password_confirme')
        if password and password_confirme and password != password_confirme :
            raise forms.ValidationError('Password do not match')
        return clean_data
    
    def save(self,commit = True):
        user = super().save(commit=False)
        email = self.cleaned_data.get('email')
        user.username = email
        password = self.cleaned_data.get('password')
        user.set_password(password)
        if commit:
            user.save()
        return user