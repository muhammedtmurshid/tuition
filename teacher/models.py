from django.db import models

# Create your models here.
from core.models import User


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField()
    place = models.CharField(max_length=255)
    phone = models.CharField(max_length=13, default='+91')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)