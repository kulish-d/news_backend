from django.contrib import admin

from news_app.models import NewsUser, NewsTag, News


admin.site.register([NewsTag, News])
