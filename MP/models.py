from django.db import models

# Create your models here.

class logins(models.Model):
    username = models.TextField(default=None)
    fname = models.TextField(default=None)
    lname = models.TextField(default=None)
    email = models.EmailField(default=None)
    password = models.CharField(default=None , max_length=120)