from rest_framework import serializers
from .models import Post, Media

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title','content']

class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = '__all__'

class PostSerializerList(serializers.ModelSerializer):
    medias = MediaSerializer(many=True, read_only=True)
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Post
        fields = '__all__'
