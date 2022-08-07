from dataclasses import fields
from logging import PlaceHolder
from tkinter import Place
from resume.models import *
from django import forms

class ContactForm(forms.ModelForm):
    name = forms.CharField(label='Full Name:', 
        widget=forms.TextInput(attrs={'class':'form-control', 'id':'name'}), 
        error_messages= {'required':'Name is required'})
    email = forms.EmailField(label='Your Email:', 
        widget=forms.EmailInput(attrs={'class':'form-control', 'id':'name'}), 
        error_messages= {'required':'email is required'})
    message = forms.CharField(label='Your Message:', 
        widget=forms.TextInput(attrs={'class':'form-control', 'id':'name'}), 
        error_messages= {'required':'message is required'})
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']