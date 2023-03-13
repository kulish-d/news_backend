from django.db import models
from django.contrib.auth import get_user_model
# from django.contrib.auth.models import User, AbstractUser

User = get_user_model()

# class User(AbstractUser):
#     pass


class Tag(models.Model):
    text = models.CharField(max_length=15)


class Post(models.Model):
    title = models.CharField(max_length=20)
    text = models.CharField(max_length=200)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    tags = models.ManyToManyField(Tag, blank=True)
