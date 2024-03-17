from django.db import models

# Create your models here.
class Designation(models.Model):
    title = models.CharField(max_length=50) 
    
    def __str__(self):
        return self.title

class Employee(models.Model):
    emp_id = models.CharField(max_length=5)  
    emp_name = models.CharField(max_length=100)  
    emp_contact = models.CharField(max_length=15)  
    emp_email = models.EmailField() 
    emp_desg= models.ForeignKey(Designation, on_delete = models.CASCADE)  