from django.core.paginator import Paginator, InvalidPage
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

from news_app.models import Post
from news_app.serializers import PostSerializer
from news.settings import NEWS_ON_PAGE


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        