from django import forms
from customer.models import Customer
from core.models import User
from customer.models import Address
from django.contrib.auth.forms import UserCreationForm


class CustomerForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['phone', 'email', 'first_name', 'last_name']

    widgets = {
        'phone': forms.TextInput(
            attrs={'name': 'phone', 'class': 'bg-warning  justify-content-center form-control', 'id': 'phone_id'}, ),
        'email': forms.EmailInput(
            attrs={'name': 'price', 'class': 'bg-warning  justify-content-center form-control', 'id': 'email_id'}, ),
        'first_name': forms.TextInput(
            attrs={'name': 'Category', 'class': 'bg-warning  justify-content-center form-control',
                   'id': 'name_id'}, ),
        'last_name': forms.TextInput(
            attrs={'name': 'Category', 'class': 'bg-warning  justify-content-center form-control',
                   'id': 'name_id'}, )
    }


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['province', 'city', 'town', 'street', 'alley', 'Plaque', 'zip_code']
