from django.http import response
from django.shortcuts import get_object_or_404, render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from post.models import Post, Category, Comment
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from post.serializers import CategoryDetailSerializer, CategorySerializer, PostCreateSerializer,\
 PostSerializer, PostDetailSerializer, CommentSerializer, CommentDetailSerializer, PostUpdateSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class MainPageView(ListView):
    model = Post
    template_name = "post/index.html"
    context_object_name = 'posts'


class PostListView(ListView):
    model = Post
    paginate_by = 8


class PostDetail(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_list'] = Comment.objects.filter(post=context['post'])
        return context
    

def show_category_list(request):
    category_list = list(Category.objects.all())
    return render(request, 'post/category_list.html', {'categories': category_list})


def each_category_posts(request, id):
    category_posts = list(Post.objects.filter(category__id = id))
    return render(request, 'post/category_posts.html', {'category_posts': category_posts})


#api/drf

@api_view(['GET'])
def post_list(request):
    if request.method == "GET":
        posts = Post.Published.all()
        serializer = PostSerializer(posts, many=True)
        return Response(data=serializer.data, status=200)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def post_detail(request, id):
    if request.method == "GET":
        post = get_object_or_404(Post, id=id)
        serializer = PostDetailSerializer(post)
        return Response(data=serializer.data, status=200)


@api_view(['GET'])
def comment_list(request):
    if request.method == "GET":
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(data=serializer.data, status=200)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def comment_detail(request, id):
    if request.method == "GET":
        comment = get_object_or_404(Comment, id=id)
        serializer = CommentDetailSerializer(comment)
        return Response(data=serializer.data, status=200)


@api_view(['GET'])
def category_list(request):
    if request.method == "GET":
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(data=serializer.data, status=200)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def category_detail(request, id):
    if request.method == "GET":
        category = get_object_or_404(Category, id=id)
        serializer = CategoryDetailSerializer(category)
        return Response(data=serializer.data, status=200)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def post_create(request):
    if request.method == 'POST':
        serializer = PostCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['author'] = request.user
        post = serializer.save()
        resp_serializer = PostSerializer(post)
        return Response(data=resp_serializer.data, status=201)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def post_update_delete(request, id):

    post = get_object_or_404(Post, id=id)

    if request.method == "GET":
        serializer = PostDetailSerializer(post)
        return Response(data=serializer.data, status=200)

    elif request.method == 'PUT':
        if post.author != request.user:
            return Response(data={'msg': 'Your are not the author of this post'}, status=400)

        serializer = PostUpdateSerializer(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        updated_post = serializer.save()
        resp_serializer = PostDetailSerializer(updated_post)
        return Response(resp_serializer.data, status=200)

    elif request.method == 'DELETE':
        if post.author != request.user:
            return Response(data={'msg': 'Your are not the author of this post'}, status=400)
        post.delete()

        return Response(status=204)