from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Contact(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=100,null=True,blank=True)
    number = models.BigIntegerField(null=True,blank=True)
    roll= models.CharField(max_length=100,null=True,blank=True)
    def __str__(self):
        return self.name

    
