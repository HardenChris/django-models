from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Snack(models.Model):

    name = models.CharField(max_length=64)
    purchaser = models.ForeignKey(get_user_model(), models.CASCADE)
    description = models.TextField(default=0)
