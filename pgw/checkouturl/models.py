from django.db import models

# Create your models here.

class testWallet(models.Model):
    number = models.IntegerField(null=False, blank=False, unique=True, max_length=11)
    pin = models.IntegerField(null=False, max_length=5)
    otp = models.IntegerField(null=False, max_length=5)
