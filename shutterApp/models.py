from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models her




class User(AbstractUser):
    is_user = models.BooleanField(default=True)



class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,related_name="user")
    Name = models.CharField(max_length=20)
    Phone = models.CharField(max_length=10)
    Email = models.EmailField()


