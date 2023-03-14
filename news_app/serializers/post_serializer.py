from rest_framework import serializers

from news_app.models import Post
from news_app.serializers.tag_serializer import TagSerializer


class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(many=False)
    tags = TagSerializer(many=True)
    class Meta:
        model = Post
        fields = '__all__'
