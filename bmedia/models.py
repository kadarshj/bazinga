from django.db import models

# Create your models here.
class ShopifyOrder(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    email = models.CharField(max_length=250,blank=True, null=True)
    closed_at = models.CharField(max_length=500,blank=True, null=True)
    created_at = models.CharField(max_length=500,blank=True, null=True)
    updated_at = models.CharField(max_length=500,blank=True, null=True)
    number = models.IntegerField(blank=True)
    note = models.CharField(max_length=500,blank=True, null=True)
    token = models.CharField(max_length=64,blank=True, null=True)
    gateway = models.CharField(max_length=250,blank=True, null=True)
    test = models.BooleanField(default=False)
    total_price = models.CharField(max_length=250,blank=True, null=True)
    subtotal_price = models.CharField(max_length=250,blank=True, null=True)
    total_weight = models.IntegerField(blank=True)
    total_tax = models.CharField(max_length=250,blank=True, null=True)
    taxes_included = models.BooleanField(default=False)
    currency = models.CharField(max_length=10,blank=True, null=True)
    financial_status = models.CharField(max_length=250,blank=True, null=True)
    confirmed = models.BooleanField(default=False)
    total_discounts = models.CharField(max_length=250,blank=True, null=True)
    total_line_items_price = models.CharField(max_length=250,blank=True, null=True)
    cart_token = models.CharField(max_length=250,blank=True, null=True)
    buyer_accepts_marketing = models.BooleanField(default=False)
    name = models.CharField(max_length=250,blank=True, null=True)
    referring_site = models.CharField(max_length=250,blank=True, null=True)
    landing_site = models.CharField(max_length=250, blank=True, null=True)
    cancelled_at = models.CharField(max_length=500, blank=True, null=True)
    cancel_reason = models.CharField(max_length=250,blank=True, null=True)
    total_price_usd = models.CharField(max_length=250,blank=True, null=True)
    checkout_token = models.CharField(max_length=250, blank=True, null=True)
    reference = models.CharField(max_length=250,blank=True, null=True)
    user_id = models.CharField(max_length=250,blank=True, null=True)
    location_id = models.CharField(max_length=250, blank=True, null=True)
    source_identifier = models.CharField(max_length=250, blank=True, null=True)
    source_url = models.CharField(max_length=250, blank=True, null=True)
    processed_at = models.CharField(max_length=250, blank=True, null=True)
    device_id = models.CharField(max_length=250, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    customer_locale = models.CharField(max_length=10,blank=True, null=True)
    app_id = models.CharField(max_length=250, blank=True, null=True)
    browser_ip = models.CharField(max_length=250, blank=True, null=True)
    landing_site_ref = models.CharField(max_length=250, blank=True, null=True)
    order_number = models.IntegerField(blank=True)
    discount_applications = models.CharField(max_length=2500,blank=True, null=True)
    discount_codes = models.CharField(max_length=1500, blank=True, null=True)
    note_attributes = models.CharField(max_length=1500, blank=True, null=True)
    payment_gateway_names = models.CharField(max_length=500, blank=True, null=True)
    processing_method = models.CharField(max_length=250,blank=True, null=True)
    checkout_id = models.CharField(max_length=250,blank=True, null=True)
    source_name = models.CharField(max_length=250,blank=True, null=True)
    fulfillment_status = models.CharField(max_length=250,blank=True, null=True)
    tax_lines = models.CharField(max_length=500,blank=True, null=True)
    tags = models.CharField(max_length=250, blank=True, null=True)
    contact_email = models.CharField(max_length=250, blank=True, null=True)
    order_status_url = models.CharField(max_length=500, blank=True, null=True)
    presentment_currency =models.CharField(max_length=250,blank=True, null=True)
    total_line_items_price_set = models.CharField(max_length=1000, blank=True, null=True)
    total_discounts_set = models.CharField(max_length=1000, blank=True, null=True)
    total_shipping_price_set = models.CharField(max_length=1000, blank=True, null=True)
    subtotal_price_set = models.CharField(max_length=1000, blank=True, null=True)
    total_price_set = models.CharField(max_length=1000, blank=True, null=True)
    total_tax_set = models.CharField(max_length=1000, blank=True, null=True)
    line_items = models.CharField(max_length=5000, blank=True, null=True)
    shipping_lines = models.CharField(max_length=1500,blank=True, null=True)
    billing_address = models.CharField(max_length=1500, blank=True, null=True)
    shipping_address = models.CharField(max_length=1500, blank=True, null=True)
    fulfillments = models.CharField(max_length=1500, blank=True, null=True)
    refunds = models.CharField(max_length=1500, blank=True, null=True)
    customer = models.CharField(max_length=2500,blank=True, null=True)












































