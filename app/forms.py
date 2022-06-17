from django import forms
from .models import Order,BuyOffer

class OrderForm(forms.ModelForm):

    class Meta:
        model=Order
        fields=('quantity','price')

class BuyForm(forms.ModelForm):

    class Meta:
        model=BuyOffer
        fields=('quantity','price')
