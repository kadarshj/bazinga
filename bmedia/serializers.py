from .models import ShopifyOrder
from rest_framework import serializers

class ShopifyOrderSerializer(serializers.ModelSerializer):
    discount_applications = serializers.JSONField()
    discount_codes = serializers.JSONField()
    note_attributes = serializers.JSONField()
    payment_gateway_names = serializers.JSONField()
    tax_lines = serializers.JSONField()
    total_line_items_price_set = serializers.JSONField()
    total_discounts_set = serializers.JSONField()
    total_shipping_price_set = serializers.JSONField()
    subtotal_price_set = serializers.JSONField()
    total_price_set = serializers.JSONField()
    total_tax_set = serializers.JSONField()
    line_items = serializers.JSONField()
    shipping_lines = serializers.JSONField()
    billing_address = serializers.JSONField()
    shipping_address = serializers.JSONField()
    fulfillments = serializers.JSONField()
    refunds = serializers.JSONField()
    customer = serializers.JSONField()


    class Meta:
        model = ShopifyOrder
        #fields = ('email','order_number','phone','total_price')
        fields = ('__all__')