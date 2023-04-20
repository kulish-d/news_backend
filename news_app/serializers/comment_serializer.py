from rest_framework import serializers

from news_app.models import Comment, Post
from news_app.serializers.user_serializer import UserSerializer


class CommentSerializer(serializers.ModelSerializer):
    # author = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
        # extra_kwargs = {
        #     'password': { 'write_only':'True' }
        # }

    # def create(self, validated_data):
    #     post = Post.objects.get(id=validated_data.pop('post'))
    #     comment = Comment.objects.create(**validated_data)
    #     comment.post.set(post)
    #     return comment