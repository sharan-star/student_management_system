from django.db import models

# Create your models here.
class Register(models.Model):
    FullName=models.CharField(max_length=30)
    UserName=models.CharField(max_length=30)
    Email=models.EmailField()
    Password=models.CharField(max_length=150)

class Student_Details(models.Model):
    Name=models.CharField(max_length=30)
    Age=models.IntegerField()
    Phone_no=models.CharField(max_length=20)
    Course=models.CharField(max_length=50)
    Resume=models.FileField(upload_to='resumes/')
    Email=models.EmailField()
    Address=models.CharField(max_length=150)

class Courses(models.Model):
    Name=models.CharField(max_length=50)
    image=models.ImageField(upload_to='images/')
    Duration=models.CharField(max_length=50)
    languages=models.CharField(max_length=50)
    Framework=models.CharField(max_length=50)
    Database=models.CharField(max_length=50)

class Drives(models.Model):
    Role=models.CharField(max_length=50)
    Company=models.CharField(max_length=50)
    Job_description=models.CharField(max_length=120)
    Location=models.CharField(max_length=50)
    starts=models.DateField()