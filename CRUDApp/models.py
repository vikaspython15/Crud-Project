from django.db import models

# Create your models here.
class Employee(models.Model):  
    cardid = models.CharField(max_length=20)  
    name = models.CharField(max_length=100)  
    email = models.EmailField()  
    contact = models.CharField(max_length=15)  
    class Meta:  
        db_table = "employee"  