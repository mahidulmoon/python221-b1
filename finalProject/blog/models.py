from distutils.command.upload import upload
from django.db import models

# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length=100,blank=False,null=True)
    description = models.TextField(blank=False,null=True)
    img_file = models.ImageField(upload_to='todo/',default="")