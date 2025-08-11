from django.db import models
from datetime import date
class treatments(models.Model):
    tname=models.CharField(max_length=100)
    timage=models.ImageField(upload_to='photos/')
    charge=models.IntegerField()
class dentist(models.Model):
    dname=models.CharField(max_length=100)
    em=models.CharField(max_length=50)
    cno=models.IntegerField()
    gender=models.CharField(max_length=10)
    photo=models.ImageField(upload_to='photos/')
    quali=models.CharField(max_length=50)
    uname=models.CharField(max_length=50)
    pword=models.CharField(max_length=50)
    rights=models.CharField(max_length=50,default='ND')
class userreg(models.Model):
    fname = models.CharField(max_length=100)
    em = models.CharField(max_length=50)
    cno = models.IntegerField()
    gender = models.CharField(max_length=10)
    uname = models.CharField(max_length=50)
    pword = models.CharField(max_length=50)
    rights = models.CharField(max_length=50, default='U')
class booking(models.Model):
    bno = models.IntegerField()
    bdate = models.DateField(default=date.today)
    rdate = models.DateField()
    did= models.IntegerField(default=0)
    dname= models.CharField(max_length=50)
    pid= models.IntegerField(default=0)
    patient=models.CharField(max_length=100,default='x')
    tname=models.CharField(max_length=100)
    charge=models.IntegerField(default=0)
    status=models.CharField(max_length=50,default='New Booking')
# Create your models here.
