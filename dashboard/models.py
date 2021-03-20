from django.db import models

# Create your models here.
class Profile(models.Model):
    user_id=models.IntegerField()
    role=models.IntegerField()
    name=models.CharField(max_length=255)

class Messages(models.Model):
    sender_id=models.IntegerField()
    reciever_id=models.IntegerField()
    application_id=models.IntegerField()
    message=models.CharField(max_length=255)
    timestamp=models.DateTimeField(auto_now=True)
    public=models.BooleanField(default=True)