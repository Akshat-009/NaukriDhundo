from django.db import models
import helpers
# Create your models here.
class Jobs(models.Model):
    title=models.CharField(max_length=255)
    jobdescription=models.CharField(max_length=255)
    #qualification=models.CharField(max_length=255)
    salary=models.IntegerField()
    mode=models.CharField(max_length=122)
    profile=models.IntegerField()
    slug=models.CharField(max_length=25,default=helpers.rand_str)
class Qualification(models.Model):
    job_id=models.IntegerField()
    name=models.CharField(max_length=30)
