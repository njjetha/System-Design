from django.db import models

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    # shipping_address =
    # billing_address  =

class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    class Meta:
        abstract = True

class ShippingAddress(Address):
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        related_name="shipping_address"
    )