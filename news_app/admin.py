from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from news_app.models import User, Post, Tag


class MyUserAdmin(UserAdmin):
    ordering = ['id']
    list_display=['username','email']


admin.site.register(User, MyUserAdmin)
admin.site.register([Post, Tag])
