from .models import ShopifyOrder
from django import forms

class ShopifyOrderForms(forms.ModelForm):

    class Meta:
        model = ShopifyOrder
        fields = ['email','phone']
