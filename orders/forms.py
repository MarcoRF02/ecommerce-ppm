from django import forms
from .models import Order
import re

from django import forms
from .models import Order

from datetime import datetime
from django.core.exceptions import ValidationError

from django.db.models.functions import Now
"""
class CheckoutForm(forms.ModelForm):
   class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'address', 'card_number', 'card_expiry', 'card_cvv']
        widgets = {

            'card_number': forms.PasswordInput(),
            'card_cvv': forms.PasswordInput(),
            'card_expiry': forms.DateInput(
               format=('%Y-%m-%d'),
               attrs={'class': 'form-control',
                       'placeholder': 'Select a date',
                       'type': 'date'
                       }),
        }
        
"""

class MonthYearWidget(forms.TextInput):
    def __init__(self, attrs=None):
        default_attrs = {'class': 'form-control', 'placeholder': 'MM/YY', 'pattern': '(0[1-9]|1[0-2])/[0-9]{2}'}
        if attrs:
            default_attrs.update(attrs)
        super().__init__(attrs=default_attrs)

class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'address', 'card_number', 'card_expiry', 'card_cvv']
        widgets = {
            'card_number': forms.PasswordInput(),
            'card_cvv': forms.PasswordInput(),
            'card_expiry': MonthYearWidget(attrs={'id': 'id_card_expiry'}),
        }

    def clean_card_expiry(self):
        card_expiry = self.cleaned_data['card_expiry']
        try:
            # Adjust the input format for two-digit years
            expiry_date = datetime.strptime(card_expiry, '%m/%y')
        except ValueError:
            raise ValidationError('Invalid date format. Use MM/YY.')

        # Get the current date and set it to the first day of the current month
        now = datetime.now()
        first_of_current_month = datetime(now.year, now.month, 1)

        if expiry_date < first_of_current_month:
            raise ValidationError('The expiry date must be in the future.')

        return card_expiry

    def clean_card_number(self):
        card_number = self.cleaned_data['card_number']
        if not re.match(r'^\d{16}$', card_number):
            raise ValidationError('Card number must be exactly 16 digits.')
        return card_number

    def clean_card_cvv(self):
        card_cvv = self.cleaned_data['card_cvv']
        if not re.match(r'^\d{3}$', card_cvv):
            raise ValidationError('CVV must be exactly 3 digits.')
        return card_cvv











"""
class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['address', 'payment_method']
        
"""
