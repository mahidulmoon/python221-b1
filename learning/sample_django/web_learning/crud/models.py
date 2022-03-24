from operator import mod
from django.db import models

# Create your models here.

class Office(models.Model):
    company_name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    img_up = models.ImageField(upload_to="images/",default="")