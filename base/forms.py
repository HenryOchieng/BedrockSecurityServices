from django.core.mail import send_mail, get_connection

from django.forms.widgets import TextInput, Textarea, EmailInput

from django import forms

class ContactForm(forms.Form):
   name = forms.CharField(label='sr-only', widget=forms.TextInput(
   attrs={'placeholder': 'Name', 'class': 'form-control', 'id':'c_name'}), required=True)

   email = forms.EmailField(label='sr-only', widget=forms.EmailInput(
   attrs={'placeholder': 'E-mail', 'class': 'form-control', 'id':'c_email'}),
   required=True)

   message = forms.CharField(label='sr-only', widget=forms.Textarea(
   attrs={'placeholder': 'Message', 'class': 'form-control', 'id':'c_message'}), required=True)