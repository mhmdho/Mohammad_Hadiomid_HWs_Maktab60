from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.generics import get_object_or_404

from blog.models import Post

from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response

from blog.serializers import PostSerializer, PostDetailSerializer, PostCreateSerializer, PostUpdateSerializer


@api_view(['GET', 'POST'])
def post_list_create(request):
    if request.method == 'GET':
        posts = Post.objects.filter(published=True).all()
        serializer = PostSerializer(posts, many=True)

        return Response(data=serializer.data, status=200)

    elif request.method == 'POST':
        serializer = PostCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        post = serializer.save()

        post.creator = request.user
        post.save()

        resp_serializer = PostSerializer(post)
        return Response(data=resp_serializer.data, status=201)


@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([])
def post_detail_update_delete(request, id):
    # try:
    #     post = Post.objects.get(id=id)
    # except Post.DoesNotExist:
    #     return Response(status=status.HTTP_404_NOT_FOUND)

    post = get_object_or_404(Post, id=id)

    if request.method == "GET":
        serializer = PostDetailSerializer(post)
        return Response(data=serializer.data, status=200)

    elif request.method == 'PUT':
        if post.creator != request.user:
            return Response(data={'msg': 'this post owned by another user'}, status=400)

        serializer = PostUpdateSerializer(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        updated_post = serializer.save()
        resp_serializer = PostDetailSerializer(updated_post)
        return Response(resp_serializer.data, status=200)

    elif request.method == 'DELETE':
        if post.creator != request.user:
            return Response(data={'msg': 'this post owned by another user'}, status=400)
        post.delete()

        return Response(status=204)

