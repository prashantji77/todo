from django.db import models


# Create your models here.
class product(models.Model):
    item=models.CharField(max_length=100)
    price=models.FloatField()
    description=models.TextField()
