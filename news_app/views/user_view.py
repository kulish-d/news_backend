from rest_framework.views import APIView
from news_app.serializers import UserSerializer, PostSerializer
from news_app.models import Post
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer


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
                            'user_email': request.user.email
                            })

class PeopleView(APIView):
    def get(self, request):
        post_id = request.GET.get('post_id')
        return Response()