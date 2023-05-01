from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

import json

from news_app.models import Post, Comment
from news_app.serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # def retrieve(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     print(instance)
    #     comments = Comment.objects.filter(post=instance)
    #     print(comments)
    #     serializer = self.get_serializer(instance)
    #     return Response(serializer.data)

    def create(self, request):
        good_data = request.data.dict()
        good_data['tags'] = json.loads(good_data['tags'])
        good_data['tags'] = list(map(lambda tag: {'text': tag}, good_data['tags']))
        serializer = self.get_serializer(data=good_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, pk, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        good_data = request.data.dict()
        good_data['tags'] = json.loads(good_data['tags'])
        good_data['tags'] = list(map(lambda tag: {'text': tag}, good_data['tags']))
        serializer = self.get_serializer(instance, data=good_data, partial=partial)
        if serializer.is_valid():
            serializer.save(author=self.request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
