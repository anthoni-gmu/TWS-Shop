from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User

from .models import UserAccount

class AccountForm(forms.ModelForm):
    address = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-2 text-sm border rounded-md focus:border-blue-400 focus:outline-none focus:ring-1 focus:ring-blue-600',
            'placeholder': 'Adrress'
        }), required=True
    )
    zipcode = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-2 text-sm border rounded-md focus:border-blue-400 focus:outline-none focus:ring-1 focus:ring-blue-600',
            'placeholder': 'Codigó zip'
        }), required=True
    )
    place = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-2 text-sm border rounded-md focus:border-blue-400 focus:outline-none focus:ring-1 focus:ring-blue-600',
            'placeholder': 'Place'
        }), required=True
    )
    phone = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-2 text-sm border rounded-md focus:border-blue-400 focus:outline-none focus:ring-1 focus:ring-blue-600',
            'placeholder': 'Phone'
        }), required=True
    )
    class Meta:
        model=UserAccount
        fields='__all__'
        exclude=('user',)
       
        


class SignUpForm(UserCreationForm):
   
    
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-2 text-sm border rounded-md focus:border-blue-400 focus:outline-none focus:ring-1 focus:ring-blue-600',
            'placeholder': 'First_name'
        }), required=True
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-2 text-sm border rounded-md focus:border-blue-400 focus:outline-none focus:ring-1 focus:ring-blue-600',
            'placeholder': 'Last_name'
        }), required=True
    )
    email = forms.EmailField(
        widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-2 text-sm border rounded-md focus:border-blue-400 focus:outline-none focus:ring-1 focus:ring-blue-600',
            'placeholder': 'Email'
        }), required=True
    )
    
    password1 = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-2 text-sm border rounded-md focus:border-blue-400 focus:outline-none focus:ring-1 focus:ring-blue-600',
            'placeholder': 'Password1',
            'type': 'password'
            
        }), required=True
    )
    password2 = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-2 text-sm border rounded-md focus:border-blue-400 focus:outline-none focus:ring-1 focus:ring-blue-600',
            'placeholder': 'Password2',
            'type': 'password'
        }), required=True
    )
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-2 text-sm border rounded-md focus:border-blue-400 focus:outline-none focus:ring-1 focus:ring-blue-600',
            'placeholder': 'Username'
        }), required=True
    )
   
    
    class Meta:
        model =User
        fields=['username', 'first_name', 'last_name', 'email','password1','password2']