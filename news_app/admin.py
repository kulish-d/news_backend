from django.contrib import admin

from news_app.models import User, Post, Tag, Comment

admin.site.register(User)
admin.site.register([Post, Tag, Comment])
