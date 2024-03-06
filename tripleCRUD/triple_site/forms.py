from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 

class addTriple(forms.Form):
    subject = forms.CharField(label='subject', max_length=100)
    predicate = forms.CharField(label='predicate', max_length=100)
    object = forms.CharField(label='object', max_length=100)

class RegisterForm(UserCreationForm):
    model = User
    fields = [
        "username",
        "password1",
        "password2",
    ]

class UploadFileForm(forms.Form):
    excel_file = forms.FileField()