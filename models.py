from django.db import models
from datetime import date
# Create your models here.


class homepageItem(models.Model):
    created_at = models.DateField(default=date.today)
    name = models.CharField(max_length=200)
    zahlen = models.FloatField()
