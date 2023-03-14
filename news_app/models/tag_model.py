from django.db import models


class Tag(models.Model):
    text = models.CharField(max_length=15)
