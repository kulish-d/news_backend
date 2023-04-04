from django.db import models
from news_app.models.user_model import User
from news_app.models.tag_model import Tag


class Post(models.Model):
    title = models.CharField(max_length=20)
    text = models.CharField(max_length=200)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    tags = models.ManyToManyField(Tag, blank=True)
    image = models.ImageField(upload_to='img/', default='img/default_user.png')
