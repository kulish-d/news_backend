from rest_framework import serializers

from news_app.models import Comment, Post
from news_app.serializers.user_serializer import UserSerializer


class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
