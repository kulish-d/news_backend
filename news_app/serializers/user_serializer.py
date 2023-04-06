from rest_framework import serializers

from news_app.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'password', 'avatar')

    def create(self, validated_data):
        print(validated_data)
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, data):
        print(data)
        instance.username = data.get('username', instance.username)
        instance.email = data.get('user_email', instance.email)
        instance.avatar = data.get('user_avatar', instance.avatar)
        instance.save()
        return instance
