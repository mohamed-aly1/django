from django.db import models
# Create your models here.


class MyUserModel (models.Model):
    Username= models.CharField(max_length=100 ,null=True) 
    Email= models.CharField(max_length=100 ,null=True) 
    Password= models.CharField(max_length=100 ,null=True) 
    Phone= models.CharField(max_length=100 ,null=True) 
    pic= models.ImageField(null=True , blank=True)
    Address= models.CharField(max_length=100 ,null=True) 

    def __str__(self) :
        return str(self.Username)
  
   
class Cart(models.Model):
    user = models.CharField(max_length=30)
    product = models.CharField(max_length=30)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
 
class Product(models.Model):
    name = models.CharField(max_length=30)
    price = models.CharField(max_length=30)
    photo = models.ImageField(null=True , blank=True)
          