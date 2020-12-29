# [TODO] Create class for forms
from django import forms

class ClientForm(forms.Form):
    client_name = forms.CharField(label='Name:', max_length=100)
    inquiry_reason = forms.CharField(widget=forms.Textarea, label='Reason for inquiry:', max_length=100)
    contact_number = forms.CharField(label='Contact Number:', max_length=100)