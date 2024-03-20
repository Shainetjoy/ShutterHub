from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models her




class User(AbstractUser):
    is_user = models.BooleanField(default=False)
    is_Manufacturers = models.BooleanField(default=False)
    is_Sales = models.BooleanField(default=False)




class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,related_name="user")
    Name = models.CharField(max_length=20)
    Phone = models.CharField(max_length=10)
    Email = models.EmailField()


catagory = (
    ('Wood','Wood'),
    ('PVC','PVC'),
    ('Steel','Steel'),
)
class ShutterDtls(models.Model):
    product_Id = models.AutoField(unique=True,primary_key=True)
    product_Name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    category = models.CharField(max_length=100,choices=catagory)#add catagry(e.g., wooden shutters, vinyl shutters, etc.)
    Material = models.CharField(max_length=100) #( wood, PVC, aluminum, etc)
    color = models.CharField(max_length=50)
    Size = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    quantity_Available = models.CharField(max_length=50)
    Manufacturer_Id = models.CharField(max_length=20)
    supplier_id = models.CharField(max_length=20)
    images = models.ImageField(upload_to='product_images/')
