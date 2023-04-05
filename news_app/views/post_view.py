from django.core.paginator import Paginator, InvalidPage
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

import json

from news_app.models import Post
from news_app.serializers import PostSerializer
from news.settings import NEWS_ON_PAGE


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def create(self, request):
        good_data = request.data.dict()
        good_data['tags'] = json.loads(good_data['tags'])
        print(good_data['tags'])
        good_data['tags'] = list(map(lambda tag: {'text': tag}, good_data['tags']))
        print(good_data)
        serializer = self.get_serializer(data=good_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        