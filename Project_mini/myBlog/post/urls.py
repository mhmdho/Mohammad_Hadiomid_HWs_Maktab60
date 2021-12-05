from django.urls import path
from post.views import PostListView, PostDetail, Register_site, change_password, each_category_posts, login_site, logout_site, search_site, show_category_list

urlpatterns = [
    path('post-list/', PostListView.as_view(), name='post-list'),
    path('post-detail/<slug:slug>', PostDetail.as_view(), name='post_detail'),

    path('category-list/', show_category_list, name='category-list'),
    path('category-posts/<int:id>', each_category_posts, name = 'category_to_posts'),
    # path('',MainPageView.as_view()),

    path('login/', login_site, name='login_url'),
    path('logout/', logout_site, name='logout_url'),
    path('register/', Register_site, name='register_url'),
    path('changepassword/', change_password, name='change_password_url'),

    path('search/', search_site, name='search_url'),

]
