from django.urls import path
from post.views import PostListView, PostDetail, each_category_posts, show_category_list

urlpatterns = [
    path('post-list/', PostListView.as_view(), name='post-list'),
    path('post-detail/<slug:slug>', PostDetail.as_view(), name='post_detail'),

    path('category-list/', show_category_list, name='category-list'),
    path('category-posts/<int:id>', each_category_posts, name = 'category_to_posts'),
    # path('',MainPageView.as_view()),



]
