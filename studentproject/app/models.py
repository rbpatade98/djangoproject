from django.db import models

# Create your models here.
class student(models.Model):
    sid=models.PositiveBigIntegerField(primary_key=True)
    name=models.CharField(max_length=100)
    emailid=models.EmailField(max_length=20)