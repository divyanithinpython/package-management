from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone




# Create your models here.

class Pakage(models.Model):
    location  =models.CharField(max_length=100)
    image=models.ImageField(upload_to='image/')
    image1=models.ImageField(upload_to='image/',default=True)
    image2=models.ImageField(upload_to='image/',default=True)
    
    price=models.IntegerField()
    start_date=models.DateField(default=timezone.now)
    end_date=models.DateField(default=timezone.now)
    shortdescription=models.TextField()
    total_seats=models.IntegerField(default=0)
    available_seats=models.IntegerField(default=0)
    fulldescription=models.TextField()
    approved=models.BooleanField('Approved',default=False)

    def is_expired(self):
        return self.end_date < timezone.now().date()
    def calculate_available_seats(self):
        booked_seats=TravelBook.objects.filter(destination=self).aggregate(total=sum('seats'))['total']
        if booked_seats is None:
           booked_seats=0
           self.available_seats=self.total_seats-booked_seats
           self.save()

class Profile(models.Model):
      user=models.OneToOneField(User,on_delete=models.CASCADE)
      first_name=models.CharField(max_length=100,default=0)
      last_name=models.CharField(max_length=100,default=0)
      username=models.CharField(max_length=100,default=0)
      email=models.EmailField(default=0)
      password=models.CharField(max_length=100,default=True)
      



    
   
        


class VendorRegister(models.Model):
    Vendorname=models.CharField(max_length=50)
    Email=models.EmailField()
    Password=models.CharField(max_length=50)
    ConfirmPassword=models.CharField(max_length=50,default=True)

class TravelBook(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)

    email=models.EmailField()
    phone=models.IntegerField()
    destination=models.CharField(max_length=50)
    seats=models.IntegerField(default=1)

    package = models.ForeignKey(Pakage, on_delete=models.CASCADE,null=True,blank=True)
    
    
    
    
    
    