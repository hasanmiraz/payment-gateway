from django.db import models

# Create your models here.
class Tokens(models.Model):
    grant_token = models.TextField()
    time_token_created = models.TimeField()