from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import *

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
		# exclude = ['date_created']

class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2']
        