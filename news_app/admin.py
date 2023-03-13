from django.contrib import admin

from news_app.models import Post, Tag


admin.site.register([Post, Tag])
