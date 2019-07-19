from django.db import models

# Create your models here.
class plac(models.Model):
    code=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    des=models.TextField()

    price=models.IntegerField() 
    offer=models.BooleanField(default=False)


class itenary(models.Model):
    code=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    day1=models.TextField()
    day2=models.TextField()
    day3=models.TextField()
    day4=models.TextField()
    day5=models.TextField()


class clients(models.Model):
    
    First_name=models.CharField(max_length=100)
    aadhar_number=models.TextField()
    No_of_adults=models.IntegerField()
    no_of_children=models.IntegerField()
