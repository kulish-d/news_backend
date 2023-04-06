from django.core import serializers
from rest_framework.views import APIView
from rest_framework.response import Response

from news_app.serializers import UserSerializer, PostSerializer
from news_app.models import Post, User
from news.settings import MEDIA_URL

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class UserView(APIView):
    def get(self, request):
        return Response({'user_id': request.user.id,
                         'username': request.user.username,
                         'user_email': request.user.email,
                         'user_avatar': f'{MEDIA_URL}{str(request.user.avatar)}',
                         })


class PeopleView(APIView):
    def get(self, request):
        user_id = request.GET.get('id')
        user = User.objects.get(id=user_id)
        serializer = UserSerializer(user)
        returned_data = serializer.data
        del returned_data['password']
        return Response(returned_data)
