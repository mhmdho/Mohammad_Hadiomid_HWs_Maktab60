

from django.urls import path
from blog.views import post_list, post_detail

urlpatterns = [
    path('post/', post_list, name='post_list'),
    path('post/<int:post_id>', post_detail, name='post_detail')

]