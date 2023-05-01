from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListAPIView

from news_app.models import Comment, User
from news_app.serializers import CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(author=User.objects.get(id=request.data['author'])) 
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

# class CommentView(ListAPIView):
#     def get(self, request):
#         comments = Comment.objects.filter(post=request.GET.get('post'))
#         res_com = []
#         for comment in comments:
#             serializer = CommentSerializer(data=comments)
#             serializer.is_valid(raise_exception=True)
#             res_com.append(serializer.data)
#         print(res_com)
#         return Response(serializer.data)
