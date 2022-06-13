from  django.forms import ModelForm
from .models import *


class  ContactRequestForm(ModelForm):
    class Meta:
        model = ContactRequest
        fields = ['email', 'name', 'content']
