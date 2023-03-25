from django.db import models

# Create your models here.

class testWallet(models.Model):
    number = models.PhoneNumberField(null=False, blank=False, unique=True)
    pin = models.IntegerField(null=False, max_length=5)
    otp = models.ImageField(null=False, max_length=5)
