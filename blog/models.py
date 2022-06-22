from email.policy import default
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.


class Post(models.Model):
    Title = models.CharField(max_length=200, blank=False, null=False)
    Text = models.TextField()

    Created_date: models.DateTimeField(auto_now_add=True)
    Published_date = models.DateTimeField(auto_now_add=True)
