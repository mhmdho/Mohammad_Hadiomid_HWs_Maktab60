from rest_framework import serializers

from blog.models import Post
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'first_name', 'last_name']


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'created']


class PostDetailSerializer(serializers.ModelSerializer):
    creator = UserSerializer()
    class Meta:
        model = Post
        fields = ['id', 'title', 'created', 'creator']


