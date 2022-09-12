from django.db import models

# Create your models here.

class Register(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=250)
    confirm_password = models.CharField(max_length=250)