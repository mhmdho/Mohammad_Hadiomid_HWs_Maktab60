from django.urls import path
from post.views import PostListView, PostDetail, category_detail, category_list, each_category_posts, post_create, post_update_delete, show_category_list
from post.views import post_list, post_detail, comment_list, comment_detail


urlpatterns = [
    path('post-list/', PostListView.as_view(), name='post-list'),
    path('post-detail/<slug:slug>', PostDetail.as_view(), name='post_detail'),

    path('category-list/', show_category_list, name='category-list'),
    path('category-posts/<int:id>', each_category_posts, name = 'category_to_posts'),
    # path('',MainPageView.as_view()),

    path('post/', post_list, name='post_list_api'),
    path('post/<int:id>/', post_detail, name='post_detail_api'),
    path('comment/', comment_list, name='comment_list_api'),
    path('comment/<int:id>/', comment_detail, name='comment_detail_api'),
    path('category/', category_list, name='category_list_api'),
    path('category/<int:id>/', category_detail, name='category_detail_api'),
    path('createpost/', post_create, name='createpost_api'),
    path('updatedeletepost/<int:id>/', post_update_delete, name='updatedeletepost_api'),


]