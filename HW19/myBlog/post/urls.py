from django.urls import path
from post.views import CategoryDetailUpdateDeleteView, CategoryListCreate, CommentDetailUpdateDeleteView, CommentListCreate,\
     PostDetailUpdateDeleteView, PostListCreate, TagDetailUpdateDeleteView, TagListCreate


urlpatterns = [

    # api
    path('post/', PostListCreate.as_view(), name='post_list_api'),
    path('post/<int:pk>/', PostDetailUpdateDeleteView.as_view(), name='post_detail_api'),
    path('tag/', TagListCreate.as_view(), name='tag_list_api'),
    path('tag/<int:pk>/', TagDetailUpdateDeleteView.as_view(), name='tag_detail_api'),
    path('category/', CategoryListCreate.as_view(), name='category_list_api'),
    path('category/<int:pk>/', CategoryDetailUpdateDeleteView.as_view(), name='category_detail_api'),
    path('comment/', CommentListCreate.as_view(), name='comment_list_api'),
    path('comment/<int:pk>/', CommentDetailUpdateDeleteView.as_view(), name='comment_detail_api'),

]