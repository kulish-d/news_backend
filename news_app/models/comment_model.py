from django.db import models
from news_app.models.user_model import User
from news_app.models.post_model import Post


class Comment(models.Model):
    text = models.CharField(max_length=30)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    post = models.ForeignKey(Post, null=True, on_delete=models.CASCADE)
