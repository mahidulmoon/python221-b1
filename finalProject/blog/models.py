from datetime import datetime
from distutils.command.upload import upload
from time import timezone
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.utils.timezone import now
from datetime import datetime


class Todo(models.Model):
    title = models.CharField(max_length=100,blank=False,null=True)
    description = models.TextField(blank=False,null=True)
    img_file = models.ImageField(upload_to='todo/',default="")
    date_time = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)
