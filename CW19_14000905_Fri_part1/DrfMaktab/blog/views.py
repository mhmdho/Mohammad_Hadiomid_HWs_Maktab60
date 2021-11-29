from django.shortcuts import render

# Create your views here.
from blog.models import Post

from rest_framework.decorators import api_view
from rest_framework.response import Response

from blog.serializers import PostSerializer, PostDetailSerializer


@api_view(['GET'])
def post_list(request):

    posts = Post.objects.filter(published=True).all()
    serializer = PostSerializer(posts, many=True)

    return Response(data=serializer.data, status=200)


@api_view(['GET'])
def post_detail(request, post_id):

    post = Post.objects.get(id=post_id)
    serializer = PostDetailSerializer(post)

    return Response(data=serializer.data, status=200)