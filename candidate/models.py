from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class job(models.Model):
    title = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    description = models.TextField()
    posted_by = models.ForeignKey(User , on_delete = models.CASCADE)

