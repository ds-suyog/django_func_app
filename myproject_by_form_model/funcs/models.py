from django.db import models

# Create your models here.
class UserInput(models.Model):
    factorial = models.CharField(max_length=3)
    fibonacci = models.CharField(max_length=3)
    armstrong = models.CharField(max_length=10)
    palindrome = models.CharField(max_length=100)
