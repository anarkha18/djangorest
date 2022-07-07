from django.db import models

# Create your models here.
class Userdata(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phone=models.IntegerField()
    dob=models.DateField()
    gender=models.CharField(max_length=8)
    department=models.CharField(max_length=20, blank=True)
    course=models.CharField(max_length=50)

def __str__(self):
    return self.name


