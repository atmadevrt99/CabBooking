from django.db import models

# Create your models here.
class contact(models.Model):
    name=models.CharField(max_length=100)
    contact=models.CharField(max_length=20)
    email=models.CharField(max_length=120)
    message=models.CharField(max_length=600)
    def __str__(self):
        return self.name

class profile(models.Model):
    name=models.CharField(max_length=120)
    dob=models.DateField()
    mobile=models.CharField(max_length=20)
    email=models.EmailField(max_length=80,primary_key=True)
    passwd=models.CharField(max_length=100)
    address=models.TextField(max_length=2000)
    myfile=models.ImageField(upload_to='static/profile/',default="")

    def __str__(self):
        return self.name

class booking(models.Model):
    trip=models.CharField(max_length=100)
    tour=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    dob = models.DateField()
    contact=models.CharField(max_length=20)
    email=models.CharField(max_length=120)
    vechile=models.CharField(max_length=50)
    pas=models.IntegerField(max_length=10)
    message=models.CharField(max_length=600)
    def __str__(self):
        return self.name

