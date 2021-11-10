from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(max_length=120)
    phone = models.CharField(max_length=12)
    entry = models.BooleanField()

    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(max_length=120)
    phone = models.CharField(max_length=12)

    def __str__(self):
        return self.name

