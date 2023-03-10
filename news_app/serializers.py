from rest_framework import serializers

from news_app.models import NewsUser, NewsTag, News


class NewsTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsTag
        fields = '__all__'


class NewsSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(many=False)
    tags = NewsTagSerializer(many=True)
    class Meta:
        model = News
        fields = '__all__'
