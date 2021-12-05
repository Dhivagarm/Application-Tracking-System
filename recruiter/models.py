from django.db import models
from candidate.models import job
from django.contrib.auth.models import User

# Create your models here.

class application(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    job_id = models.ForeignKey(job, on_delete=models.CASCADE)
    resume = models.FileField()
    match = models.FloatField()