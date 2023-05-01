from rest_framework import serializers

from news_app.models import Post, Tag, Comment
from news_app.serializers.tag_serializer import TagSerializer
from news_app.serializers.user_serializer import UserSerializer

class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    tags = TagSerializer(many=True)
    class Meta:
        model = Post
        fields = '__all__'



    def create(self, validated_data):
        post_tags = []
        for tag in validated_data.pop('tags'):
            post_tags.append(Tag.objects.get_or_create(text=tag.get('text'))[0])
                  
        post = Post.objects.create(**validated_data)

        post.tags.set(post_tags)
        return post
    
    def update(self, instance, data):
        post_tags = []
        for tag in data.pop('tags'):
            post_tags.append(Tag.objects.get_or_create(text=tag.get('text'))[0])
        instance.title = data.get('title', instance.title)
        instance.text = data.get('text', instance.text)
        instance.tags.set(post_tags)
        instance.image = data.get('image', instance.image)
        instance.save()
        return instance