from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


from post.models import Post, Category, Comment
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

