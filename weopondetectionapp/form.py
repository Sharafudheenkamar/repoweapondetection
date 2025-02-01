from django import forms
from .models import *


class UserForm(forms.ModelForm):
    class   Meta:
        model=LoginTable

        fields=['username','password','usertype','name','email','phonenumber']
class Sentreplyform(forms.ModelForm):
    class Meta:
        model=Complaint
        fields=['reply']