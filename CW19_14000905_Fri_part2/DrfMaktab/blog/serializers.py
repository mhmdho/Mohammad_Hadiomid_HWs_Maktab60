from django.contrib.auth import get_user_model
from rest_framework import serializers

from blog.models import Post, Tag

User = get_user_model()


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class PostSerializer(serializers.ModelSerializer):
    tag = TagSerializer()
    creator = UserSerializer()

    class Meta:
        model = Post
        fields = ['id', 'title', 'created', 'tag', 'creator']


class PostDetailSerializer(serializers.ModelSerializer):
    creator = UserSerializer()
    tags = TagSerializer(many=True)
    tag = TagSerializer()

    class Meta:
        model = Post
        fields = ['id', 'title', 'created', 'creator', 'tags', 'tag']

class PostCreateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=225) 

    def create(self, validate_data):
        return Post(**validate_data)
