from rest_framework import generics

from news_app.models import User, Post
from news_app.serializers import PostSerializer

class UserPostsView(generics.ListAPIView):
    serializer_class = PostSerializer
    
    def get_queryset(self):
        user_id = self.kwargs.get('user_id')
        queryset = Post.objects.filter(author=user_id)
        return queryset.order_by('-id')
