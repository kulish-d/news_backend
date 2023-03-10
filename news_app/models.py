from django.db import models
from django.contrib.auth import get_user_model
# from django.contrib.auth.models import User, AbstractUser

NewsUser = get_user_model()

# class NewsUser(AbstractUser):
#     pass


class NewsTag(models.Model):
    text = models.CharField(max_length=15)


class News(models.Model):
    title = models.CharField(max_length=20)
    text = models.CharField(max_length=200)
    author = models.ForeignKey(NewsUser, null=True, on_delete=models.SET_NULL)
    tags = models.ManyToManyField(NewsTag, blank=True)
