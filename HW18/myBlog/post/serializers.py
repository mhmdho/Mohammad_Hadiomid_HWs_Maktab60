from django.contrib.auth import get_user_model
from rest_framework import serializers

from post.models import Category, Post, Tag, Comment


User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer()

    class Meta:
        model = Post
        fields = ['id', 'title', 'created_at', 'author']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'owner', 'description', 'post_id']


class CategoryDetailSerializer(serializers.ModelSerializer):
    posts = PostSerializer(source='category_posts', many=True)

    class Meta:
        model = Category
        fields = ['id', 'title', 'posts']


class PostDetailSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    tag = TagSerializer(many=True)
    category = CategorySerializer(many=True)
    comment = CommentSerializer(source='post_comment', many=True)

    class Meta:
        model = Post
        fields = '__all__'


class CommentDetailSerializer(serializers.ModelSerializer):
    owner = UserSerializer()
    post = PostSerializer()

    class Meta:
        model = Comment
        fields = '__all__'


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'tag', 'category']


class PostUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'tag', 'category']