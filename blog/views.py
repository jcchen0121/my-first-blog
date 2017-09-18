from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.db import models
from .models import Post
from .forms import PostForm
from django.shortcuts import redirect # https://tutorial.djangogirls.org/en/django_forms/
from django.contrib.auth.models import User

# Create your views here.

# https://tutorial.djangogirls.org/en/django_views/
# https://tutorial.djangogirls.org/en/dynamic_data_in_templates/
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

# https://tutorial.djangogirls.org/en/extend_your_application/
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

# https://tutorial.djangogirls.org/en/django_forms/
# from django.shortcuts import redirect
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

# https://tutorial.djangogirls.org/en/django_forms/
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})