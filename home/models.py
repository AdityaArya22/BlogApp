from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class userData(models.Model):
    user = models.ForeignKey(User, on_delete = models.SET_NULL, null = True , blank = True) 
    username = models.TextField(default = 'username')
    desc = models.TextField(default='SOME STRING')
    pic = models.ImageField(upload_to='pics', null=True , blank = True)


# models.py

# blog/models.py


class Comment(models.Model):
    user_data = models.ForeignKey(userData, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)


