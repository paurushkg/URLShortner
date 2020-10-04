from rest_framework import serializers
from shortner.models import Url


class UrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Url
        fields = '__all__'


class PostUrlSerializer(serializers.Serializer):
    link = serializers.CharField(max_length=4096)
