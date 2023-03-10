from django.core.paginator import Paginator, InvalidPage
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

from news_app.models import NewsUser, NewsTag, News
from news_app.serializers import NewsTagSerializer, NewsSerializer
from news.settings import NEWS_ON_PAGE


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    