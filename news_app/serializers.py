from rest_framework import serializers

from news_app.models import User, Post, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(many=False)
    tags = TagSerializer(many=True)
    class Meta:
        model = Post
        fields = '__all__'
