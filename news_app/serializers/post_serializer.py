from rest_framework import serializers

from news_app.models import Post, Tag
from news_app.serializers.tag_serializer import TagSerializer
from news_app.serializers.user_serializer import UserSerializer

class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    tags = TagSerializer(many=True)
    class Meta:
        model = Post
        fields = '__all__'


    def create(self, validated_data):
        tags_data = validated_data.pop('tags')
        post = Post.objects.create(**validated_data)

        for tag in tags_data:
            Tag.objects.create(post=post, **tag)

        return post
