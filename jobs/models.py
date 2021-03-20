from django.db import models

# Create your models here.
class Applicant(models.Model):
    applicant_id=models.IntegerField()
    job_id=models.IntegerField()
    resume=models.FileField(default="")
    experiences=models.CharField(max_length=255)
    expectations=models.CharField(max_length=255)
    cover=models.CharField(max_length=255)
    status=models.IntegerField() #0 for pending #1 accepted # 2  rejected