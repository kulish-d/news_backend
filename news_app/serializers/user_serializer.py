from rest_framework import serializers

from news_app.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'password', 'avatar')
        extra_kwargs = {
            'password': { 'write_only':'True' }
        }

    def create(self, validated_data):
        print(validated_data)
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, data):
        instance.username = data.get('username', instance.username)
        instance.email = data.get('email', instance.email)
        instance.avatar = data.get('avatar', instance.avatar)
        instance.save()
        return instance
