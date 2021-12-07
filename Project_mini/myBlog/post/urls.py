from django.urls import path
from post.views import PostListView, PostDetail, Register_site, add_category, add_tag, change_password,\
                    delete_category, each_category_posts, each_tag_posts, login_site, logout_site, search_site,\
                    show_category_list, show_tag_list, edit_category

urlpatterns = [
    path('post-list/', PostListView.as_view(), name='post-list'),
    path('post-detail/<slug:slug>', PostDetail.as_view(), name='post_detail'),

    path('category-list/', show_category_list, name='category-list'),
    path('category-posts/<int:id>', each_category_posts, name = 'category_to_posts'),
    # path('',MainPageView.as_view()),
    path('tag-list/', show_tag_list, name='tag-list'),
    path('tag-posts/<int:id>', each_tag_posts, name = 'tag_to_posts'),


    path('login/', login_site, name='login_url'),
    path('logout/', logout_site, name='logout_url'),
    path('register/', Register_site, name='register_url'),
    path('changepassword/', change_password, name='change_password_url'),

    path('add_category/', add_category, name='add_category_url'),
    path('add_tag/', add_tag, name='add_tag_url'),
    path('delete_category/<int:id>',delete_category, name="delete_category_url"),
    path('edit_category/<int:id>',edit_category, name="edit_category_url"),

    path('search/', search_site, name='search_url'),

]
