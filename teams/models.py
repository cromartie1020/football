from django.db import models
from datetime import datetime

class Team(models.Model):
    name = models.CharField(max_length = 250,unique=True,blank=False)
    location= models.CharField(max_length=255,blank=False)
    created=models.DateTimeField(auto_now_add=True)
    updated =models.DateTimeField(auto_now=datetime.now)
    logo=models.ImageField(upload_to='images/', default='default.jpg')   
    
    def __str__(self):
        
        return f"{self.location} {self.name}"



