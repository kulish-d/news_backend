from rest_framework.views import APIView
from news_app.serializers import UserSerializer
from news_app.models import User
from rest_framework.response import Response


class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def get(self, request):
        user_id = request.GET.get('id')
        user = User.objects.get(id=user_id)
        return Response({'user': user.username})
