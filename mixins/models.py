from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length = 50)
    age = models.IntegerField()
    regd_no = models.CharField(max_length = 10)
    city = models.CharField(max_length = 50)

