from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['product', 'name', 'last_name', 'phone', 'shipping_address']
