
from post.filter import PostListFilter

from post.models import Post, Category, Comment, Tag
from rest_framework.response import Response
from post.serializers import CategoryDetailSerializer, CategorySerializer, CommentCreateSerializer, PostCreateSerializer, PostSerializer,\
     PostDetailSerializer, CommentSerializer, CommentDetailSerializer, PostUpdateSerializer, TagDetailSerializer, TagSerializer
from rest_framework.permissions import IsAuthenticated

from rest_framework import generics, status


# Create your views here.

#api


# -----------post----------- #

class PostListCreate(generics.ListCreateAPIView):
    queryset = Post.Published.all()
    permission_classes = (IsAuthenticated,)
    filterset_class = PostListFilter

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PostSerializer
        elif self.request.method == 'POST':
            return PostCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        post = self.perform_create(serializer)
        resp_serializer = PostSerializer(post)
        headers = self.get_success_headers(serializer.data)
        return Response(resp_serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        return serializer.save()


class PostDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):

    def get_queryset(self):
        if self.request.method == 'GET':
            queryset = Post.Published.all()
        else:
            queryset = Post.Published.filter(author=self.request.user)
        return queryset

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PostDetailSerializer
        else:
            return PostUpdateSerializer


# -----------tag----------- #

class TagListCreate(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = TagSerializer

class TagDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = TagDetailSerializer


# -----------category----------- #

class CategoryListCreate(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = CategorySerializer

class CategoryDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = CategoryDetailSerializer


# -----------comment----------- #

class CommentListCreate(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = CommentSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CommentSerializer
        elif self.request.method == 'POST':
            return CommentCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        comment = self.perform_create(serializer)
        resp_serializer = CommentSerializer(comment)
        headers = self.get_success_headers(serializer.data)
        return Response(resp_serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        return serializer.save()


class CommentDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CommentDetailSerializer
    
    def get_queryset(self):
        if self.request.method == 'GET':
            queryset = Comment.objects.all()
        else:
            queryset = Comment.objects.filter(owner=self.request.user)
        return queryset
