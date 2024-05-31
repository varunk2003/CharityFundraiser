from django.db import models
class user(models.Model):
    username=models.CharField(max_length=255)
    email=models.EmailField()
    password1=models.CharField(max_length=255)

class log(models.Model):
    signins=models.BooleanField(default=False)
    username=models.CharField(max_length=255)
    emailid=models.EmailField()
