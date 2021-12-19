from django import forms
from Do_an_01 import models


class FormContact(forms.ModelForm):
    name = forms.CharField(label='Name', max_length=150, widget=forms.TextInput(attrs={
        "class": "form-control fh5co_contact_text_box",
        "placeholder": "Enter Your Name",
        "required": "required",
    }))
    email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={
        "class": "form-control fh5co_contact_text_box",
        "placeholder": "Email",
        "required": "required",
    }))
    subject = forms.CharField(label='Subject', max_length=400, widget=forms.TextInput(attrs={
        "class": "form-control fh5co_contact_text_box",
        "placeholder": "Subject",
        "required": "required",
    }))
    message = forms.CharField(label='Message', widget=forms.Textarea(attrs={
        "class": "form-control fh5co_contacts_message",
        "placeholder": "Message",
        "required": "required",
    }))

    class Meta:
        model = models.Contact
        fields = '__all__'
        exclude = ['submit_day']
