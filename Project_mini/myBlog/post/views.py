from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from django.urls import reverse

from post.models import Post, Category, Comment

from .forms import ChangePasswordForm, LoginForm, RegisterForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

from django.db.models.query_utils import Q
from django.contrib.auth.models import User 

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

@login_required(redirect_field_name='next', login_url='login_url')
def each_category_posts(request, id):
    category_posts = list(Post.objects.filter(category__id = id))
    return render(request, 'post/category_posts.html', {'category_posts': category_posts})


def login_site(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request,username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                next = request.GET.get('next')
                try:
                    return redirect(next)
                except:              
                    return redirect('index')
            #if loged in cannot redirect to login.
            else :
                print('not found user') #add messege
            # redirect to a new URL:
            return render(request, 'forms/login.html', {'form': form})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = LoginForm()

    return render(request, 'forms/login.html', {'form': form})


def logout_site(request):
    logout(request)
    return redirect('login_url')


def Register_site(request):
    form = RegisterForm(None or request.POST)
    if request.method == "POST":
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            return HttpResponse('user registered')

    return render(request, 'forms/register.html', {'form':form})


def search_site(request):
    if request.method == "GET":
        search = request.GET.get('search_box')
        posts = Post.Published.filter(Q(title__icontains=search) |
                                    Q(descrption__icontains=search))
    return render(request, 'post/search.html', {'posts': posts})

@login_required(login_url='login_url')
def change_password(request):
    form = ChangePasswordForm()
    if request.method == "POST":
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            user = request.user
            print('u', user)
            if user.check_password(form.cleaned_data.get('old_password')):
                user.set_password(form.cleaned_data.get('new_password'))
                user.save()
                return redirect('login_url')

    return render(request, 'forms/change_password.html', {'form': form})

