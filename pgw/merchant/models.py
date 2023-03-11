from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Merchant(AbstractUser):
    wallet = models.CharField(max_length=11, unique=True)
    merchant_name = models.TextField()
