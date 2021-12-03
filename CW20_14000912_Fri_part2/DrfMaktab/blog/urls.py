

from django.urls import path
from blog.views import post_list_create, post_detail_update_delete

urlpatterns = [
    path('post/', post_list_create, name='post_list'),
    path('post/<int:id>/', post_detail_update_delete, name='post_detail')
]