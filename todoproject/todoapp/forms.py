from django.forms import models

from .models import Task
from django import forms
class todoForms(models.ModelForm):
    class Meta:
        model=Task
        fields=['name','priority','date']

