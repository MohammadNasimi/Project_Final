from django import forms
from customer.models import Customer
from core.models import User
from django.contrib.auth.forms import UserCreationForm


class CustomerForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['phone', 'email', 'first_name', 'last_name']
