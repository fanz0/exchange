from django import forms
from .models import Order
from .models import SellOrder

class OrderForm(forms.ModelForm):

    class Meta:
        model=Order
        fields=('quantity','price')

class SellOrderForm(forms.ModelForm):

    class Meta:
        model=SellOrder
        fields=('buyer_quantity','buyer_price')