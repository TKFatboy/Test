from django.db import models

# Create your models here.

class Member(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

class Comment(models.Model):
    comment = models.CharField(max_length=255)
