from django.db import models

# Create your models here.
class LoginTable(models.Model):
    username=models.CharField(max_length=100,null=True,blank=True)
    password=models.CharField(max_length=100,null=True,blank=True)
    usertype=models.CharField(max_length=100,null=True,blank=True)
    name=models.CharField(max_length=100,null=True,blank=True)
    phonenumber=models.BigIntegerField(null=True,blank=True)
    email=models.CharField(max_length=100,null=True,blank=True)




class Feedback(models.Model):
    USER=models.ForeignKey(LoginTable, on_delete=models.CASCADE)
    feedback=models.CharField(max_length=1000,null=True,blank=True)
    date=models.DateField(auto_now_add=True)

class Complaint(models.Model):
    USER=models.ForeignKey(LoginTable, on_delete=models.CASCADE)
    complaint=models.CharField(max_length=1000,null=True,blank=True)
    date=models.DateField(auto_now_add=True)
    reply=models.CharField(max_length=1000,null=True,blank=True)
    
class image(models.Model):
    image=models.FileField(upload_to='weopons/',null=True,blank=True)

from django.db import models
from django.utils.timezone import now

class Notification(models.Model):
    message = models.CharField(max_length=255)
    detected_at = models.DateTimeField(default=now)
    image = models.ImageField(upload_to='detections/', blank=True, null=True)

    def __str__(self):
        return f"Weapon detected at {self.detected_at}"
                
        
    
    