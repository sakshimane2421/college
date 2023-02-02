from django import forms
from .models import *

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'mobile_number', 'email_address', 'message')


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'