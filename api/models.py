
from django.db import models

# Create your models here.
class Note(models.Model):
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]

    class Meta:
        ordering = ['-updated']


#made chnage from here
class profiles(models.Model):
    uid=models.CharField(max_length=50,default='')
    password = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    name = models.CharField(max_length=80, default='name')
    phone = models.CharField(max_length=80, default='813-xxx-xxxx')
    address = models.CharField(max_length=80, default='abc street')
    picUrl = models.CharField(max_length=200, default='xyz.jpeg')
    workingHours = models.CharField(max_length=30, default='6-12am')
    city = models.CharField(max_length=80, default='tampa')

    def __str__(self):
        return self.name

