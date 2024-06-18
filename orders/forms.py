from django import forms
from .models import Order

from django import forms
from .models import Order

class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'address', 'card_number', 'card_expiry', 'card_cvv']
        widgets = {
            'card_number': forms.PasswordInput(),
            'card_cvv': forms.PasswordInput(),
        }

"""
class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['address', 'payment_method']
        
"""
