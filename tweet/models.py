from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=210)
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.TextField(max_length=250)
    photo = models.ImageField(upload_to="photos/", blank=True,null=True)
    updated_at = models.DateTimeField(auto_now=True)

def __str__(self):
    return f'{self.user.username} - {self.text[:10]}'



