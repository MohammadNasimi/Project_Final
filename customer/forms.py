from django import forms
from customer.models import Customer
from core.models import User
from django.contrib.auth.forms import UserCreationForm


class CustomerForm(UserCreationForm):
    address = forms.CharField(max_length=15, min_length=10)

    class Meta:
        model = User
        fields = ['phone', 'password', 'first_name', 'last_name', 'email']
