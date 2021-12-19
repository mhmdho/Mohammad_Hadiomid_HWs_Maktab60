

from django.urls import path
from blog.views import PostDetails, PostList

urlpatterns = [
    path('post/', PostList.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetails.as_view(), name='post_detail')
]