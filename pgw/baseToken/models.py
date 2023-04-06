from django.db import models

# Create your models here.
class Tokens(models.Model):
    grant_token = models.TextField(unique=True, max_length=30)
    time_token_created = models.TimeField()
    phone = models.IntegerField(unique=True, max_length=11)