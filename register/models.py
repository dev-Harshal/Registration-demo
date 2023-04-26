from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=13)
    city = models.CharField(max_length=100)
    choose=(('male', 'male'),('female', 'female'))
    gender = models.CharField(max_length=10,choices=choose)

    def __str__(self):
        return self.name
    