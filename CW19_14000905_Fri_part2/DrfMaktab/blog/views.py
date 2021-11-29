from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.generics import get_object_or_404

from blog.models import Post

from rest_framework.decorators import api_view
from rest_framework.response import Response

from blog.serializers import PostSerializer, PostDetailSerializer, PostCreateSerializer


@api_view(['GET', 'POST'])
def post_list(request):
    if request.method == 'GET':
        posts = Post.objects.filter(published=True).all()
        serializer = PostSerializer(posts, many=True)

        return Response(data=serializer.data, status=200)
    elif request.method == 'POST':
        serializer = PostCreateSerializer(data=request.data)
        if serializer.is_valid():
            post = serializer.save()
            

        resp_serializer = PostSerializer(post)
        return Response(data=serializer.data, status=200)

@api_view(['GET'])
def post_detail(request, id):
    # try:
    #     post = Post.objects.get(id=id)
    # except Post.DoesNotExist:
    #     return Response(status=status.HTTP_404_NOT_FOUND)

    post = get_object_or_404(Post, id=id)

    serializer = PostDetailSerializer(post)

    return Response(data=serializer.data, status=200)
