from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin

from news_app.models import User, Post, Tag


# class MyUserAdmin(UserAdmin):
#     ordering = ['id']
#     list_display=['email']

admin.site.register(User)
admin.site.register([Post, Tag])
