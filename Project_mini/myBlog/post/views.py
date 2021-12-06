from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from django.urls import reverse

from post.models import Post, Category, Comment, Tag

from .forms import AddCategoryForm, AddTagForm, ChangePasswordForm, LoginForm, RegisterForm
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
    new_category = request.GET.get('category_box')
    form = AddCategoryForm(None or new_category)
    if form.is_valid():
        form.save()
        return redirect(reverse('category-list'))
    category_list = Category.objects.all()
    return render(request, 'post/category_list.html', {'categories': category_list, 'form_cat':form})

@login_required(redirect_field_name='next', login_url='login_url')
def each_category_posts(request, id):
    category_posts = Post.objects.filter(category__id = id)
    return render(request, 'post/category_posts.html', {'category_posts': category_posts})


def show_tag_list(request):
    new_tag = request.GET.get('tag_box')
    form = AddCategoryForm(None or new_tag)
    if form.is_valid():
        form.save()
        return redirect(reverse('tag-list'))
    tag_list = Tag.objects.all()
    return render(request, 'post/tag_list.html', {'tags': tag_list, 'form_tag': form})

def each_tag_posts(request, id):
    tag_posts = Post.objects.filter(tag__id = id)
    return render(request, 'post/tag_posts.html', {'tag_posts': tag_posts})


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


def search_site(request):
    if request.method == "GET":
        search = request.GET.get('search_box')
        posts = Post.Published.filter(Q(title__icontains=search) |
                                    Q(descrption__icontains=search))
    return render(request, 'post/search.html', {'posts': posts})


@login_required(login_url='/post/login')
def add_category(request):
    # if request.method == "GET":
    #     new_category = request.GET.get('category_box')
    #     categry = Category.objects.create(title=new_category.cleaned_data['title'])
    # return render(request,'post/category_list.html', {'form_cat':categry})

    form = AddCategoryForm(None or request.POST)
    if form.is_valid():
        form.save()
            #messages.add_message(request, messages.ERROR, f'تگ مورد نظر ذخیره گردید.',extra_tags="danger")
        return redirect(reverse('category-list'))

    return render(request,'forms/add_category.html',{'form_cat':form})


@login_required(login_url='/post/login')
def add_tag(request):
    form = AddTagForm(None or request.POST)
    if form.is_valid():
        form.save()
            #messages.add_message(request, messages.ERROR, f'تگ مورد نظر ذخیره گردید.',extra_tags="danger")
        return redirect(reverse('tag-list'))

    return render(request,'forms/add_tag.html',{'form_tag':form})
